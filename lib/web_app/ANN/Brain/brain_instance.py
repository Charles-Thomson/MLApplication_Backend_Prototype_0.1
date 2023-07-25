"""Instance of a brain used by a agent"""
import base64
import numpy as np
from ANN.config import config
import pickle


class BrainInstance:
    """Instance of agent brian"""

    def __init__(
        self,
        brain_id,
        generation_num,
        hidden_weights,
        output_weights,
        fitness,
        traversed_path,
        fitness_by_step,
    ):
        self.brain_id: str = brain_id
        self.generation_num: int = generation_num
        self.hidden_weights: np.array = hidden_weights
        self.output_weights: np.array = output_weights
        self.fitness: float = fitness
        self.traversed_path: list[int] = traversed_path
        self.fitness_by_step: np.array = fitness_by_step

    def set_attributes_to_bytes(self) -> None:
        """Covert the np.arrays to bytes for DB storage"""

        self.hidden_weights = self.hidden_weights.tobytes()
        self.output_weights = self.output_weights.tobytes()
        self.traversed_path = bytes(self.traversed_path)
        self.fitness_by_step = self.fitness_by_step.tobytes()

    def get_attributes_from_bytes(self) -> None:
        """Convert the weights from bytes to np.arrays"""

        # reshape would be 24, -1 i think ?
        self.hidden_weights = np.frombuffer(self.hidden_weights).reshape(9, 3)
        self.output_weights = np.frombuffer(self.output_weights)
        self.traversed_path = list(self.traversed_path)
        self.fitness_by_step = np.frombuffer(self.fitness_by_step)

    def determin_action(self, sight_data: np.array) -> int:
        """Determin best action based on given data/activation"""

        # This needs refactoring to be taken in at the build of the instance, not ref to config
        hidden_layer_activation_function = config.HIDDEN_LAYER_ACTIVATION_FUNCTION
        output_layer_activation_function = config.OUPUT_LAYER_ACTIVATION_FUNCTION

        hidden_layer_dot_product = np.dot(sight_data, self.hidden_weights)

        vectorize_func = np.vectorize(hidden_layer_activation_function)
        hidden_layer_activation = vectorize_func(hidden_layer_dot_product)

        output_layer_dot_product = np.dot(hidden_layer_activation, self.output_weights)

        return output_layer_activation_function(output_layer_dot_product)
