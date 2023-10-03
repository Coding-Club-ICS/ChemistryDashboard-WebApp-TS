import os
import requests
import periodictable
import pubchempy as pcp
from mendeleev import element
from chempy import balance_stoichiometry
from flask_cors import CORS
from flask import Flask, jsonify, request, json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

cors = CORS(app)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['CORS_HEADERS'] = 'Content-Type'


valid_elements = [element.symbol for element in periodictable.elements]





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
    app.run()
