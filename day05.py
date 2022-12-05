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

stacks = [
    ['F', 'T', 'N', 'Z', 'M', 'G', 'H', 'J'],
    ['J', 'W', 'V'],
    ['H', 'T', 'B', 'J', 'L', 'V', 'G'],
    ['L', 'V', 'D', 'C', 'N', 'J', 'P', 'B'],
    ['G', 'R', 'P', 'M', 'S', 'W', 'F'],
    ['M', 'V', 'N', 'B', 'F', 'C', 'H', 'G'],
    ['R', 'M', 'G', 'H', 'D'],
    ['D', 'Z', 'V', 'M', 'N', 'H'],
    ['H', 'F', 'N', 'G']
]

stacks_R = [
    ['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
    ['V', 'W', 'J'],
    ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
    ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
    ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
    ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
    ['D', 'H', 'G', 'M', 'R'],
    ['H', 'N', 'M', 'V', 'Z', 'D'],
    ['G', 'N', 'F', 'H']
]


with open("puzzles/day05_moves.txt", "r") as f:
    moves = f.read().replace('\n', 'xxx').split("xxx")

moves = [move.replace("move ", "").replace(" from ", "-").replace(" to ", "-") for move in moves]

stacks = stacks_R.copy()
for no, move in enumerate(moves, 1):
    n, from_, to = move.split("-")
    n, from_, to = int(n), int(from_) - 1, int(to) - 1

    # to_be_moved = stacks[from_][:n].copy()
    # to_be_moved.reverse()  # rm for part two
    # stacks[from_] = stacks[from_][n:]
    # stacks[to] = to_be_moved + stacks[to]

    to_be_moved = stacks[from_][-n:].copy()
    #to_be_moved.reverse()
    stacks[from_] = stacks[from_][:-n]
    stacks[to] = stacks[to] + to_be_moved

print(''.join([stack[0] for stack in stacks]))
print(''.join([stack[-1] for stack in stacks]))
"""
TDCHVHJTG
NGCMPJLHV
"""
raise Exception



""" OLD """

stacks = {
1: ["J", "H", "G", "M", "Z", "N", "T", "F"],
2: ["V", "W", "J"],
3: ["G", "V", "L", "J" "B", "T", "H"],
4: ["B", "P", "J", "N", "C", "D", "V", "L"],
5: ["F", "W", "S", "M", "P", "R", "G"],
6: ["G", "H", "C", "F", "B", "N", "V", "M"],
7: ["D", "H", "G", "M", "R"],
8: ["H", "N", "M", "V", "Z", "D"],
9: ["G", "N", "F", "H"]
}
print(stacks)

with open("puzzles/day05_moves.txt", "r") as f:
    moves = f.read().replace('\n', 'xxx').split("xxx")

# stacks = {
# 1: ["Z", "N"], 2:["M", "C", "D"], 3:["P"]
# }

# with open("puzzles/day05_example_moves.txt", "r") as f:
#     moves = f.read().replace('\n', 'xxx').split("xxx")

moves = [move.replace("move ", "").replace(" from ", "-").replace(" to ", "-") for move in moves]
print(moves)
print(len(moves))

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
print(stacks)

print("".join([stack[-1] for stack in stacks.values()]))

"""
TDCHVHJTG
NGCMPJLHV
"""
