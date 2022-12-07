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

pt1 = sum(to_be_summed)

points_shape = {"A": 1, "B": 2, "C": 3}

strategy = {
    ("A", "X"): "C",
    ("A", "Y"): "A",
    ("A", "Z"): "B",
    ("B", "X"): "A",
    ("B", "Y"): "B",
    ("B", "Z"): "C",
    ("C", "X"): "B",
    ("C", "Y"): "C",
    ("C", "Z"): "A",
}
outcomes = {
    ("A", "A"): 3,
    ("A", "B"): 6,
    ("A", "C"): 0,
    ("B", "A"): 0,
    ("B", "B"): 3,
    ("B", "C"): 6,
    ("C", "A"): 6,
    ("C", "B"): 0,
    ("C", "C"): 3,
}

to_be_summed = []
for game in data:
    opponent, my_goal = game.split("x")
    me = strategy.get((opponent, my_goal))
    points = points_shape.get(me) + outcomes.get((opponent, me))
    to_be_summed.append(points)

pt2 = sum(to_be_summed)

print("Part1:", pt1)
print("Part2:", pt2)
