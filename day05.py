"""
[F]         [L]     [M]            
[T]     [H] [V] [G] [V]            
[N]     [T] [D] [R] [N]     [D]    
[Z]     [B] [C] [P] [B] [R] [Z]    
[M]     [J] [N] [M] [F] [M] [V] [H]
[G] [J] [L] [J] [S] [C] [G] [M] [F]
[H] [W] [V] [P] [W] [H] [H] [N] [N]
[J] [V] [G] [B] [F] [G] [D] [H] [G]
 1   2   3   4   5   6   7   8   9 
"""

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
}

with open("puzzles/day05_moves.txt", "r") as f:
    moves = f.read().replace('\n', 'xxx').split("xxx")

# stacks = {
# 1: ["Z", "N"], 2:["M", "C", "D"], 3:["P"]
# }

# with open("puzzles/day05_example_moves.txt", "r") as f:
#     moves = f.read().replace('\n', 'xxx').split("xxx")

moves = [move.replace("move ", "").replace(" from ", "-").replace(" to ", "-") for move in moves]
debug = False
for no, move in enumerate(moves, 1):
    n, from_, to = move.split("-")
    n, from_, to = int(n), int(from_), int(to)
    if debug:
        print(no)
        print(n, from_, to)
        print(stacks)
    to_be_moved = stacks[from_][-n:].copy()
    # to_be_moved.reverse()  # not for Pt Two
    stacks[to] = stacks[to] + to_be_moved
    stacks[from_] = stacks[from_][:-n]

print("".join([stack[-1] for stack in stacks.values()]))
