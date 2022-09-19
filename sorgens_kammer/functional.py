from typing import List, Any, Union
from functools import reduce

l: List[Union[int, Any]] = [6, 5, 0, 3, 5, 1, 2, 3, 5, 4, 5, 6, 6, 5, 7, 5, 5, 10, 5, 0]
s = 'abcdefg'

# map: apply function to sequence
print('--- map ---')
print(list(map(lambda x: x ** 5, l)))

# map: make new sequence out of two (shortest is the limit)
print(list(map(lambda x, y: f'{x}_{y}', l, s)))

# filter: make new sequence based on condition
print('--- filter ---')
print(list(filter(lambda x: x != 5, l)))

# zip: combine sequences into sequence of tuples (easy to generate dict)
print('--- zip ---')
print(list(zip(l, s)))
print(dict(zip(l, s)))

# reduce: a certain cumulative effect on sequence items
print('--- reduce ---')
print(reduce(lambda x, y: f'{x}_{y}', s))
