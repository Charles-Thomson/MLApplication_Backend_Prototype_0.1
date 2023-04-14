"""Instance of a brain used by a agent"""
import numpy as np


class BrainInstance:
    """Instance of agent brian"""

    def __init__(self, brain_id, generation_num, hidden_weights, output_weights):
        self.brain_id: str = brain_id
        self.generation_num: int = generation_num
        self.hidden_weights: np.array = hidden_weights
        self.output_weights: np.array = output_weights
        self.fitness: float = 0.0
        self.traversed_path: list[int] = []

    def set_attributes_to_bytes(self) -> None:
        """Covert the np.arrays to bytes for DB storage"""
        self.hidden_weights = self.hidden_weights.tobytes()
        self.output_weights = self.output_weights.tobytes()

    def get_attributes_from_bytes(self) -> None:
        """Convert the weights from bytes to np.arrays"""
        self.hidden_weights = np.frombuffer(self.hidden_weights)
        self.output_weights = np.frombuffer(self.output_weights)
