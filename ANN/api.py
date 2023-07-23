"""
API for handling the passing of map, fitness ect data
"""
import json
from flask import Flask, request

from config import set_config
from config import config
from DataBase import database_all_brains

import main

app = Flask(__name__)


def get_payload_return_data(total_generations: int) -> dict:
    """Testing getting the needed dat from the DB"""
    payload_data: dict = {}
    for gen_val in range(total_generations + 1):
        (
            high_fitness_instance,
            low_fitness_instance,
        ) = database_all_brains.get_generation_data(gen_val)

        payload_data[f"gen_{gen_val}"] = {
            "HIGHEST_FITNESS": high_fitness_instance.fitness,
            "HIGHEST_FITNESS_PATH": high_fitness_instance.traversed_path,
            "HIGHEST_FITNESS_BY_STEP": list(high_fitness_instance.fitness_by_step),
            "LOWEST_FITNESS": low_fitness_instance.fitness,
            "LOWEST_FITNESS_PATH": low_fitness_instance.traversed_path,
            "LOWEST_FITNESS_BY_STEP": list(low_fitness_instance.fitness_by_step),
        }

    print(payload_data)

    return json.dumps(payload_data)


# Test route for payload
@app.route("/TESTPAYLOAD", methods=["GET"])
def payload_test() -> dict:
    """Testing payload"""
    print("Payload Reiceved")
    recieved_data = request.args["query"]
    data: dict = json.loads(recieved_data)

    set_config.this_set_config(data["payloadBody"])
    print(config.ENV_MAP)
    print(config.ENV_MAP.shape)

    total_generations: int = main.main_system()

    print("SYSTEM: MAIN SYSTEM RUN COMPLETE")

    json_rtn_data = get_payload_return_data(total_generations)
    # print(json_rtn_data)
    return json_rtn_data


app.run()
