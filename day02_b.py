with open("puzzles/day02.txt_02.txt", "r") as f:
    data = f.read().replace(' ', "x").replace('\n', '-').split("-")

points_shape = {"A": 1, "B": 2, "C": 3}

"""
Rock A, 
Paper B, Y
Scissor C, Z
Outcomes: 6, 3, 0

X -> I need to loose
Y -> I need to draw
Z -> I need to win
"""
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

print(sum(to_be_summed))
