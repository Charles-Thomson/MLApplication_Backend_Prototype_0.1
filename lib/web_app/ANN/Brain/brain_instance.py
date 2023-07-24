"""Instance of a brain used by a agent"""
import numpy as np

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import (
#     Column,
#     CHAR,
#     FLOAT,
# )

from ANN.config import config

# Base = declarative_base()


# Had Base as a inherited class
class BrainInstance:
    """Instance of agent brian"""

    # __tablename__ = "generations"
    # brain_id = Column("brain_id", CHAR, primary_key=True)
    # generation_num = Column("generation_num", CHAR)
    # hidden_weights = Column("hidden_weights", CHAR)
    # output_weights = Column("output_weights", CHAR)
    # fitness = Column("fitness", FLOAT)
    # traversed_path = Column("traversed_path", CHAR)
    # fitness_by_step = Column("fitness_by_step", CHAR)

    def __init__(self, brain_id, generation_num, hidden_weights, output_weights):
        self.brain_id: str = brain_id
        self.generation_num: int = generation_num
        self.hidden_weights: np.array = hidden_weights
        self.output_weights: np.array = output_weights
        self.fitness: float = 0.0
        self.traversed_path: list[int] = []
        self.fitness_by_step: np.array = np.array([])

    def set_attributes_to_bytes(self) -> None:
        """Covert the np.arrays to bytes for DB storage"""
        self.hidden_weights = self.hidden_weights.tobytes()
        self.output_weights = self.output_weights.tobytes()
        self.traversed_path = bytes(self.traversed_path)
        self.fitness_by_step = self.fitness_by_step.tobytes()

    def get_attributes_from_bytes(self) -> None:
        """Convert the weights from bytes to np.arrays"""
        # Reshape needed - from bytes flatens np.array
        self.hidden_weights = np.frombuffer(self.hidden_weights).reshape(24, -1)
        self.output_weights = np.frombuffer(self.output_weights).reshape(9, -1)
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
