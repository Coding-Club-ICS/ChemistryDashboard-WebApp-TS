import os
import requests
import periodictable
import pubchempy as pcp
from mendeleev import element
from chempy import balance_stoichiometry
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask, jsonify, request, json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = 'postgres'
DB_PORT = '5432'

DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

valid_elements = [element.symbol for element in periodictable.elements]


class Element(db.Model):
    __tablename__ = "elements"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return "Hello, World!"


@app.route("/chem/get_elements", methods=["GET"])
def get_elements():
    try:
        elements = Element.query.all()
        element_list = [{"id": element.id, "name": element.name} for element in elements]
        return jsonify({"elements": element_list})
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"}), 500


@app.route("/chem/add_element", methods=["POST"])
def add_element():
    try:
        name = request.json.get("name")
        if name not in valid_elements:
            return jsonify({"error": "Invalid element"}), 400
        element = Element(name=name)
        db.session.add(element)
        db.session.commit()
        return jsonify({"message": "Element added successfully"})
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"}), 500

with app.app_context():
    db.create_all()

@app.route("/chem/update_element/<int:id>", methods=["PUT"])
def update_element(id):
    try:
        name = request.json.get("name")
        element = Element.query.get(id)
        if element:
            element.name = name
            if name not in valid_elements:
                return jsonify({"error": "Invalid element"}), 400
            db.session.commit()
            return jsonify({"message": "Element updated successfully"})
        else:
            return jsonify({"error": "Element not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"}), 500


@app.route("/chem/delete_element/<int:id>", methods=["DELETE"])
def delete_element(id):
    try:
        element = Element.query.get(id)
        if element:
            db.session.delete(element)
            db.session.commit()
            return jsonify({"message": "Element deleted successfully"})
        else:
            return jsonify({"error": "Element not found"}), 404
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"}), 500

@app.route("/chem/balance/<string:equation>", methods=["GET"])
def balance_equation(equation):
    try:
        equation = equation.split("=")
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
        return jsonify({"error": f"Could not execute query: {e}"}), 500


@app.route("/chem/periodictable", methods=["GET"])
def get_periodic_table():
    try:
        elements = [element.symbol for element in periodictable.elements]
        return jsonify({"elements": elements})
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"}), 500

@app.route("/chem/element/<string:symbol>", methods=["GET"])
def get_properties(symbol):
    try:
        e = element(symbol)
        return jsonify({"name": e.name, "atomic_number": e.atomic_number, "atomic_weight": e.atomic_weight, "atomic_radius":e.atomic_radius})
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"}), 500


@app.route("/chem/compound/get_cid/<string:compound>", methods=["GET"])
def get_cid(compound):
    try:
        cid = requests.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound}/cids/JSON").json()["IdentifierList"]["CID"][0]
        return jsonify({"cid": cid})
    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"}), 500

    except Exception as e:
        return jsonify({"error": f"Could not execute query: {e}"}), 500
    


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
    app.run(host='0.0.0.0', port=5000, debug=True)
