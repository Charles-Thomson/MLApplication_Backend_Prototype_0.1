"""Functions usde to determin the next action"""
import numpy as np


def layer_calculation(layer_type: str, inputs: np.array, weights: np.array) -> np.array:
    """Calculate the given layer with the appropriate activaion function"""

    layer_calculated = np.dot(inputs, weights)

    match layer_type:
        case "hidden_layer":
            layer_activated = [np.maximum(0, x) for x in np.nditer(layer_calculated)]
            layer_activated = np.array(layer_activated)
        case "output_layer":
            exp_layer_calculated = np.exp(layer_calculated)
            layer_activated = exp_layer_calculated / exp_layer_calculated.sum()

    return layer_activated


def setup_determine_action(hidden_weights: np.array, output_weights: np.array):
    """Generate a curried version of the action determination for each brain insatnce"""

    def determine_action(sight_data: np.array):
        """Determine the best action given sight data"""
        hidden_layer = layer_calculation(
            layer_type="hidden_layer", inputs=sight_data, weights=hidden_weights
        )

        output_layer = layer_calculation(
            layer_type="output_layer",
            inputs=hidden_layer,
            weights=output_weights,
        )

        new_action = np.argmax(output_layer)

        return new_action

    return determine_action
