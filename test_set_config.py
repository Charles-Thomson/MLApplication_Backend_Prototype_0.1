import config
import set_config
import main

data: dict = {
    "NUMBER_OF_GENERATIONS": 10,
    "MAX_GENERATION_SIZE": 10,
    "STARTING_FITNESS_THRESHOLD": 3.0,
    "DESIERED_FIT_GENERATION_SIZE": 3,
    "ENV_MAP": [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
    "ENVIRONMENT_START_STATE": 8,
    "MAX_EPISODE_DURATION": 8,
    "WEIGHT_INITALIZATION_HEURISTIC": "he_weight_init",
    "HIDDEN_LAYER_ACTIVATION_FUNCTION": "linear_activation_function",
    "OUTPUT_LAYER_ACTIVATION_FUNCTION": "argmax_activation",
    "WEIGHTS_CROSSOVER_FUNCTIONS": "crossover_weights_average",
}


def testing_setting_of_config() -> None:
    """testing congfig"""
    print(config.NUMBER_OF_GENERATIONS)
    set_config.this_set_config(data)
    print(config.NUMBER_OF_GENERATIONS)
    print(config.ENV_MAP)
    main.main_system()


testing_setting_of_config()
