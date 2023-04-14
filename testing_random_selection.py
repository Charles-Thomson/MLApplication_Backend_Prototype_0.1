"""esting rnadom weihted slection"""

import random


elemnts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
val = len(elemnts)
weightings = tuple(val / i for i in range(1, val + 1))

selected_a, selected_b = random.choices(elemnts, weights=weightings, k=2)

print(selected_a)
print(selected_b)
print(weightings)
