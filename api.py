"""
API for handling the passing of map, fitness ect data 
"""

import json
import numpy as np
from flask import Flask, request
from main import main_system

app = Flask(__name__)


@app.route("/")
def index() -> None:
    """Basic test function"""
    return json.dumps({"name": "tesing api", "email": "email.email"})


@app.route("/test_print", methods=["GET"])
def testPrint() -> None:
    """Basic test function"""
    input_route = request.args["query"]
    print_Sent_Data(input_route)
    formatted_data = format_data(input_route)
    print(formatted_data)

    data = {"output": "", "second": ""}
    print("API accessed")
    data["output"] = ["Hello from the api"]
    data["second"] = ["Hello from the api again"]
    # return json.dumps({"name": "tesing api"})
    return data


@app.route("/run_map", methods=["GET"])
def run_map() -> dict:
    """Testing the running of a map"""
    inputroute = request.args["query"]
    map_data = format_data(inputroute)
    main_system(10, map_data)
    print("SYSTEM -- MAP RUN")


def print_Sent_Data(data) -> None:
    print(data)


def format_data(data) -> None:
    """Testing the formatting of the recived data"""
    rebuilt_list = np.fromstring(data, dtype=int, sep=",")
    rebuilt_list = np.reshape(
        rebuilt_list, (4, -1)
    )  # need to accomodate the hard coding of the shape in the passed data
    return rebuilt_list


app.run()
