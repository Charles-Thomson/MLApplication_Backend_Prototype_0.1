import json

import numpy as np


def test_json() -> None:
    """Testing json"""
    map = "1, 2, 3, 4, 5, 6, 7, 8, 9"
    value: int = 10
    func_name: str = "Activation func"

    data: dict = {"map": map, "value": value, "func_name": func_name}
    print(data)

    encoded_data = json.dumps(data)
    print(type(encoded_data))

    unencoded_data = json.loads(encoded_data)
    print(unencoded_data)
    print(type(unencoded_data))

    rtn_map = unencoded_data["map"]
    print(rtn_map)
    np_map_from_str = np.fromstring(rtn_map, dtype=int, sep=",")
    print(np_map_from_str)
    print(np_map_from_str.shape)

    reshaped_np_map = np_map_from_str.reshape(3, -1)
    print(reshaped_np_map.shape)


test_json()
