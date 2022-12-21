import utils
from dataclasses import dataclass
from typing import Tuple, List

data = utils.day_puzzle_to_list("21")
print(data)

int_str = [str(i) for i in range(1, 10)]
equations = []
known_values = dict()
for d in data:
    if any([s in int_str for s in d]):
        monkey_name, shout = d.split(": ")
        known_values[monkey_name] = int(shout)
    else:
        equations.append(d)

print(known_values)


def get_x1(eq: str) -> str:
    return eq[0:4]


def solve(eq: str):
    x1 = eq[0:4]
    x2 = eq[6:10]
    x3 = eq[13:17]
    operator = eq[11]
    print(x1, x2, x3, operator)
    x2_v = known_values.get(x2)
    x3_v = known_values.get(x3)
    if x2_v and x3_v:
        result = {"+": x2_v + x3_v,
                  "-": x2_v - x3_v,
                  "*": x2_v * x3_v,
                  "/": x2_v / x3_v,
                  }.get(operator)
        return result
    else:
        return None

to_be_solved = [get_x1(eq) for eq in equations]
solved = []

done = False
while not done:
    for eq in equations:
        x1 = get_x1(eq)
        if not known_values.get(x1):
            result = solve(eq)
            if result:
                known_values[x1] = result
                to_be_solved = [x for x in to_be_solved if x != x1]
    if to_be_solved == []:
        done = True

print(known_values)

