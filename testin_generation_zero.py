"""Testing generator for gen zero"""
from Brain.brain_generation import gen_zero_generator


def test_generation() -> object:
    """Test the calling"""
    i = gen_zero_generator(5)
    for _ in range(3):
        print("New brain requested")
        test = next(i)
        print(test.brain_id)
        print("New brain recieved")


test_generation()
