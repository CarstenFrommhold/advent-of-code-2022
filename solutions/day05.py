stacks = {
    1: ['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
    2: ['V', 'W', 'J'],
    3: ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
    4: ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
    5: ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
    6: ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
    7: ['D', 'H', 'G', 'M', 'R'],
    8: ['H', 'N', 'M', 'V', 'Z', 'D'],
    9: ['G', 'N', 'F', 'H']
}  # better parse then type in directly -> error source (!)

with open("../puzzles/day05_moves.txt", "r") as f:
    moves = f.read().replace('\n', 'xxx').split("xxx")

moves = [move.replace("move ", "").replace(" from ", "-").replace(" to ", "-") for move in moves]
debug = False


def solve(pt):
    for no, move in enumerate(moves, 1):
        n, from_, to = move.split("-")
        n, from_, to = int(n), int(from_), int(to)
        if debug:
            print(no)
            print(n, from_, to)
            print(stacks)
        to_be_moved = stacks[from_][-n:].copy()
        if pt == 1:
            to_be_moved.reverse()  # remove for Pt Two
        stacks[to] = stacks[to] + to_be_moved
        stacks[from_] = stacks[from_][:-n]
    return "".join([stack[-1] for stack in stacks.values()])


pt1 = solve(1)
pt2 = solve(2)
print("Part1:", pt1)
print("Part2:", pt2)
