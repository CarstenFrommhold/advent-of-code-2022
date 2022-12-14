import utils
from dataclasses import dataclass
from typing import Tuple, List

data = utils.day_puzzle_to_list("14")


@ dataclass
class Cord:
    x: int
    y: int


def cords_between(start: Cord, end: Cord) -> List[Cord]:
    if start.x != end.x and start.y != end.y:
        raise Exception
    elif start.x == end.x:
        if end.y >= start.y:
            r = range(start.y, end.y + 1)
        else:
            r = range(end.y, start.y + 1)
        return [Cord(start.x, i) for i in r]
    elif start.y == end.y:
        if end.x >= start.x:
            r = range(start.x, end.x + 1)
        else:
            r = range(end.x, start.x + 1)
        return [Cord(i, start.y) for i in r]


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
            cords_filled.append(Cord(x, y))
        else:
            x_prev: int = x
            y_prev: int = y
            x: int = pixel[0]
            y: int = pixel[1]
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            for between in cords_between(start=Cord(x_prev, y_prev), end=Cord(x, y)):
                cords_filled.append(between)

cords_filled = [Cord(c.x - min_x + 1, c.y) for c in cords_filled]

# Build Grid
len_y = max_y
len_x = max([c.x for c in cords_filled])
grid = [["L"] + ["." for _ in range(len_x)] for _ in range(len_y + 1)]
grid = [l + ["R"] for l in grid]
grid[0] = ["O" for _ in range(len_x + 2)]
grid.append(["U" for _ in range(len_x + 2)])

for c in cords_filled:
    grid[c.y][c.x] = "#"


def print_grid(grid: List[Cord]):
    for row in grid:
        print(row)


def get_status(candidate: Cord, grid: List[Cord]) -> str:
    return grid[candidate.y][candidate.x]


def set_snowflake(candidate: Cord, grid: List[Cord]) -> List[Cord]:
    """ snow flake comes from above @ ()"""
    if get_status(candidate, grid) in (["L, R, U"]):
        raise Exception("No place for any flakes anymore.")

    under = Cord(candidate.x, candidate.y + 1)
    left_under = Cord(candidate.x - 1, candidate.y + 1)
    right_under = Cord(candidate.x + 1, candidate.y + 1)

    if get_status(under, grid) not in (["#", "o"]):
        return set_snowflake(under, grid)
    elif get_status(left_under, grid) not in (["#", "o"]):
        return set_snowflake(left_under, grid)
    elif get_status(right_under, grid) not in (["#", "o"]):
        return set_snowflake(right_under, grid)
    else:
        grid[candidate.y][candidate.x] = "o"
        return grid


start_ = Cord(500 - min_x + 1, 1)
counter = 0
go_on = True
while go_on:
    try:
        grid = set_snowflake(start_, grid)
        counter += 1
    except:
        print_grid(grid)
        go_on = False

pt1 = counter
print("Part 1:", pt1)

