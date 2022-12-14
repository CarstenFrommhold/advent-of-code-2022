import utils
from dataclasses import dataclass
from typing import Tuple, List

data = utils.day_puzzle_to_list("14")


class Cord:
    x: int
    y: int
    val: str


def pixels_between(start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    if start[0] != end[0] and start[1] != end[1]:
        raise Exception
    elif start[0] == end[0]:
        if end[1] >= start[1]:
            r = range(start[1], end[1] + 1)
        else:
            r = range(end[1], start[1] + 1)
        return [(start[0], i) for i in r]
    elif start[1] == end[1]:
        if end[0] >= start[0]:
            r = range(start[0], end[0] + 1)
        else:
            r = range(end[0], start[0] + 1)
        return [(i, start[1]) for i in r]


min_x = 500
max_x = 500
max_y = 0
cords_filled = []
for p in data:
    to_be_drawn: List[Tuple[int]] = [eval(c) for c in p.split(" -> ")]
    for n, pixel in enumerate(to_be_drawn, 1):
        if n == 1:
            x: int = pixel[0]
            y: int = pixel[1]
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            cords_filled.append((x, y))
        else:
            x_prev: int = x
            y_prev: int = y
            x: int = pixel[0]
            y: int = pixel[1]
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            for between in pixels_between(start=(x_prev, y_prev), end=(x, y)):
                cords_filled.append(between)

print(min_x)
print(max_x)
print(max_y)
print(cords_filled)


cords_filled = [(c[0] - min_x + 1, c[1]) for c in cords_filled]
print(cords_filled)

# 500, 0 wird zu (500 + 503 - 494)
len_y = max_y
len_x = max([c[0] for c in cords_filled])
print(len_x)

grid = [["L"] + ["." for _ in range(len_x)] for _ in range(len_y + 1)]
grid = [l + ["R"] for l in grid]
grid[0] = ["O" for _ in range(len_x + 2)]
grid.append(["U" for _ in range(len_x + 2)])

for c in cords_filled:
    grid[c[1]][c[0]] = "#"

for row in grid:
    print(row)

print(len(grid))
print(len(grid[1]))

#500, 0 = 7, 0
#500, 1 = 7, 1


def get_status(candidate, grid) -> str:
    return grid[candidate[1]][candidate[0]]


def set_snowflake(candidate: Tuple[int, int], grid) -> List[List[str]]:
    """ snow flake comes from above @ ()"""
    # if candidate == (500, 1) and get_status(candidate) == "o":
    #     raise Exception("full")
    if get_status(candidate, grid) in (["L, R, U"]):
        raise Exception("vorbei")

    under = (candidate[0], candidate[1] + 1)
    left_under = (candidate[0] - 1, candidate[1] + 1)
    right_under = (candidate[0] + 1, candidate[1] + 1)

    if get_status(under, grid) not in (["#", "o"]):
        return set_snowflake(under, grid)
    elif get_status(left_under, grid) not in (["#", "o"]):
        return set_snowflake(left_under, grid)
    elif get_status(right_under, grid) not in (["#", "o"]):
        return set_snowflake(right_under, grid)
    else:
        grid[candidate[1]][candidate[0]] = "o"
        return grid

print(500 - min_x + 1)
start_ = (500 - min_x + 1, 1)
counter = 0
go_on = True
while go_on:
    try:
        grid = set_snowflake(start_, grid)
        counter += 1
    except:
        for row in grid:
            print(row)
        print("Done")
        print(counter)
        go_on = False


