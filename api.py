"""
API for handling the passing of map, fitness ect data
"""

import json
import numpy as np
from flask import Flask, request
import set_config
from DataBase import database_all_brains

import main

app = Flask(__name__)


# Add later
# Shortest Path
# Longest Path
# Each path as step by step fitness for graphs
def get_payload_return_data() -> dict:
    """Testing getting the needed dat from the DB"""
    database_all_brains.get_number_of_generations()

    data_high = database_all_brains.get_highest_fitness_from_gen(1)
    data_low = database_all_brains.get_lowest_fitness_from_gen(1)

    # print(data_high.fitness_by_step, data_low.fitness_by_step)

    return_payload = {
        "HIGHEST_FITNESS": data_high.fitness,
        "HIGHEST_FITNESS_PATH": data_high.traversed_path,
        "HIGHEST_FITNESS_BY_STEP": list(data_high.fitness_by_step),
        "LOWEST_FITNESS": data_low.fitness,
        "LOWEST_FITNESS_PATH": data_low.traversed_path,
        "LOWEST_FITNESS_BY_STEP": list(data_low.fitness_by_step),
    }

    return json.dumps(return_payload)


# Test route for payload
@app.route("/TESTPAYLOAD", methods=["GET"])
def payload_test() -> dict:
    """Testing payload"""
    print("Payload Reiceved")
    recieved_data = request.args["query"]
    data: dict = json.loads(recieved_data)

    set_config.this_set_config(data["payloadBody"])

    main.main_system()

    print("SYSTEM: MAIN SYSTEM RUN COMPLETE")

    get_payload_return_data()

    # Place Holder return data <- working

    json_rtn_data = get_payload_return_data()
    print(json_rtn_data)
    return json_rtn_data


# def format_data(data) -> None:
#     """Testing the formatting of the recived data"""
#     rebuilt_list = np.fromstring(data, dtype=int, sep=",")
#     rebuilt_list = np.reshape(
#         rebuilt_list, (4, -1)
#     )  # need to accomodate the hard coding of the shape in the passed data
#     return rebuilt_list


app.run()
