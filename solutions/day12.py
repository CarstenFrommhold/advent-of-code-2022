import utils
from typing import List
from dataclasses import dataclass
import string

heightmap = [" ".join(d).split(" ") for d in utils.day_puzzle_to_list("12", sep="--")]

len_x = len(heightmap)
len_y = len(heightmap[0])


@dataclass
class Square:
    x: int
    y: int
    distance: int


@dataclass
class Pos:
    x: int
    y: int


def calculate_minimum_distance_to_highest_square(
        heightmap: List[List[str]],
        start_square: Square) -> int:

    len_x = len(heightmap)
    len_y = len(heightmap[0])

    queue = list()
    queue.append(start_square)

    touched = [[False for _ in range(len_y)]
               for _ in range(len_x)]
    touched[start_square.x][start_square.y] = True

    while queue:
        square = queue.pop(0)

        if heightmap[square.x][square.y] == 'E':
            print("Hooray.")
            return square.distance

        # L
        if move_is_valid(square.x, square.y, square.x, square.y - 1, heightmap, touched):
            touched[square.x][square.y - 1] = True
            queue.append(Square(square.x, square.y - 1, square.distance + 1))

        # R
        if move_is_valid(square.x, square.y, square.x, square.y + 1, heightmap, touched):
            touched[square.x][square.y + 1] = True
            queue.append(Square(square.x, square.y + 1, square.distance + 1))

        # U
        if move_is_valid(square.x, square.y, square.x - 1, square.y, heightmap, touched):
            touched[square.x - 1][square.y] = True
            queue.append(Square(square.x - 1, square.y, square.distance + 1))

        # D
        if move_is_valid(square.x, square.y, square.x + 1, square.y, heightmap, touched):
            touched[square.x + 1][square.y] = True
            queue.append(Square(square.x + 1, square.y, square.distance + 1))

    return 99_999


def at_most_one_higher(to, from_) -> bool:
    return string.ascii_lowercase.index(to) - string.ascii_lowercase.index(from_) <= 1


def move_is_valid(from_x, from_y, to_x, to_y, heightmap, touched) -> bool:
    # Stay in grid
    if to_x >= len(heightmap) or to_y >= len(heightmap[0]):
        return False
    elif to_x < 0 or to_y < 0:
        return False
    elif heightmap[from_x][from_y] == "S":
        return True  # move away from start is allowed.
    elif heightmap[to_x][to_y] == "S":
        return False  # move back to start is not allowed (already touched)
    elif touched[to_x][to_y]:
        return False  # already been here
    elif touched[to_x][to_y]:
        return False  # already been here
    elif heightmap[to_x][to_y] == "E":
        if at_most_one_higher(to="z", from_=heightmap[from_x][from_y]):
            return True  # target E has the elevation z
        else:
            return False
    elif at_most_one_higher(heightmap[to_x][to_y], heightmap[from_x][from_y]):
        return True

    return False


# Pt1
# Find start
for x in range(len_x):
    for y in range(len_y):
        if heightmap[x][y] == 'S':
            start_square = Square(x, y, 0)

pt1 = calculate_minimum_distance_to_highest_square(heightmap=heightmap, start_square=start_square)


# Pt2
starts = []
for x in range(len_x):
    for y in range(len_y):
        if heightmap[x][y] == 'a':
            starts.append(Square(x, y, 0))

distances = [calculate_minimum_distance_to_highest_square(heightmap, start_square) for start_square in starts]
distances = [d for d in distances if d > 0]
pt2 = min(distances)


print("Part 1:", pt1)
print("Part 2:", pt2)
