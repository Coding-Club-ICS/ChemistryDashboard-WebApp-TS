from flask import Flask, jsonify, request
import psycopg2
from psycopg2 import sql
import os

app = Flask(__name__)

DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_PORT = os.environ["DB_PORT"]

def create_db_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        return connection
    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
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
            connection.close()


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
        return jsonify({"error": f"Could not execute query: {e}"})
    finally:
        if connection:
            connection.close()


@app.post("/chem/add_element")
def insert_element():
    connection = create_db_connection()

    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500
    try:
        cursor = connection.cursor()

        data = request.json
        name = data.get("name")

        if name is None:
            return jsonify({"error": "Name is required"}), 400

        insert_query = "INSERT INTO elements.elements (name) VALUES (%s)"
        cursor.execute(insert_query, (name,))

        connection.commit()

        return jsonify({"message": "Element added successfully"})
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"})
    finally:
        if connection:
            connection.close()

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
        return jsonify({"error": f"Could not execute query: {e}"})
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    create_tables()
    app.run()
