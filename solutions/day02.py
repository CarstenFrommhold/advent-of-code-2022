with open("../puzzles/day02.txt", "r") as f:
    data = f.read().replace(' ', "x").replace('\n', '-').split("-")

points_shape = {"X": 1, "Y": 2, "Z": 3}

outcomes = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}

to_be_summed = []
for game in data:
    opponent, me = game.split("x")
    points = points_shape.get(me) + outcomes.get((opponent, me))
    to_be_summed.append(points)

print(sum(to_be_summed))
