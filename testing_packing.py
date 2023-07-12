import struct
import numpy as np


def test_struct():
    data = []
    test: np.array = np.array(data)
    test_bytes = test.tobytes()

    rtn_data = np.frombuffer(test_bytes)
    print(rtn_data)


test_struct()
