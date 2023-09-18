import os
import psycopg2
import psycopg2.pool
from chempy import balance_stoichiometry
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, jsonify, request, json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

db_connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    host=os.environ["DB_HOST"],
    database=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    port=os.environ["DB_PORT"]
)


def create_db_connection():
    try:
        return db_connection_pool.getconn()
    except psycopg2.Error as e:
        app.logger.error("Error: Could not connect to database")
        return None


def create_tables():
    connection = create_db_connection()

    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS elements.elements (id SERIAL PRIMARY KEY, name VARCHAR(50))")

        connection.commit()
        print("Tables created successfully")
    except Exception as e:
        print("Error: Could not create table")
        print(e)
    finally:
        if connection:
            db_connection_pool.putconn(connection)


class ElementForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])

@app.route("/")
def index():
    return "Hello, World!"


@app.get("/chem/get_elements")
def get_data():
    connection = create_db_connection()

    if connection is None:
        return jsonify({"error": "Could not connect to database"}), 500
    try:
        cursor = connection.cursor()
        query = """
SELECT * FROM elements.elements
ORDER BY id ASC
"""
        cursor.execute(query)

        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        app.logger.error(f"Could not execute query: {e}")
        return jsonify({"error": f"Could not execute query: {e}"})
    finally:
        if connection:
            db_connection_pool.putconn(connection)


@app.post("/chem/add_element")
def insert_element():
    connection = create_db_connection()

    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500
    try:
        cursor = connection.cursor()

        form = ElementForm()

        data = request.json
        name = data.get("name")


        insert_query = "INSERT INTO elements.elements (name) VALUES (%s)"
        cursor.execute(insert_query, (name,))

        connection.commit()

        return jsonify({"message": "Element added successfully"})
    except Exception as e:
        app.logger.error(f"Could not execute query: {e}")
        return jsonify({"error": f"Could not execute query: {e}"})
    finally:
        if connection:
            db_connection_pool.putconn(connection)


@app.put("/chem/update_element/<int:id>")
def update_element(id):
    connection = create_db_connection()

    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500
    try:
        cursor = connection.cursor()

        data = request.json
        name = data.get("name")

        if name is None:
            return jsonify({"error": "Name is required"}), 400

        update_query = "UPDATE elements.elements SET name = %s WHERE id = %s"
        cursor.execute(update_query, (name, id))

        connection.commit()

        return jsonify({"message": "Element updated successfully"})
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"})
    finally:
        if connection:
            connection.close()


@app.delete("/chem/delete_element/<int:id>")
def delete_element(id):
    connection = create_db_connection()

    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500
    try:
        cursor = connection.cursor()

        delete_query = "DELETE FROM elements.elements WHERE id = %s"
        cursor.execute(delete_query, (id,))

        connection.commit()

        return jsonify({"message": "Element deleted successfully"})
    except Exception as e:
        app.logger.error(f"Could not execute query: {e}")
        return jsonify({"error": f"Could not execute query: {e}"}), 500
    finally:
        if connection:
            db_connection_pool.putconn(connection)

@app.get("/chem/balance/<string:equation>")
def balance_equation(equation):
    try:
        equation = equation.split("=")
        equation = equation.replace(" ", "")
        reactants = set(equation[0].split("+"))
        products = set(equation[1].split("+"))
        reac, prod = balance_stoichiometry(reactants, products)
        reac = dict(reac)
        prod = dict(prod)
        result = ""
        reac_key = list(reac.keys())
        prod_key = list(prod.keys())

        for key in reac_key:
            if reac[key] == 1:
                reac[key] = ""
            result += str(reac[key]) + key
            if key != reac_key[-1]:
                result += " + "

        for key in prod_key:
            if prod[key] == 1:
                prod[key] = ""
            result += " = " + str(prod[key]) + key
            if key != prod_key[-1]:
                result += " + "

        return jsonify({"result": result})
    except Exception as e:
        print(e)

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    create_tables()
    app.run()
