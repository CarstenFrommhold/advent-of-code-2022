import utils
from dataclasses import dataclass

data = utils.day_puzzle_to_list("09")
moves = [d.split(" ") for d in data]


@dataclass
class Cord:
    x: int
    y: int


def touch(head: Cord, tail: Cord) -> bool:
    if abs(head.x - tail.x) < 2:
        return abs(head.y - tail.y) < 2
    elif abs(head.y - tail.y) < 2:
        return abs(head.x - tail.x) < 2
    else:
        return False


def adjust_tail(head: Cord, tail: Cord) -> Cord:
    if not touch(head, tail):
        if head.y == tail.y:
            if head.x - tail.x == 2:  # right
                tail.x += 1
            elif head.x - tail.x == -2:  # left
                tail.x -= 1
        elif head.x == tail.x:
            if head.y - tail.y == 2:  # up
                tail.y += 1
            elif head.y - tail.y == -2:  # down
                tail.y -= 1
        # diagonal
        elif head.y > tail.y:
            if head.x > tail.x:
                tail.x += 1
                tail.y += 1
            elif head.x < tail.x:
                tail.x -= 1
                tail.y += 1
        elif head.y < tail.y:
            if head.x > tail.x:
                tail.x += 1
                tail.y -= 1
            elif head.x < tail.x:
                tail.x -= 1
                tail.y -= 1
    return tail


def solve(pt: int):

    head = Cord(0, 0)
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = [Cord(0, 0) for _ in range(9)]
    print(t2)
    tail_positions = [(0, 0)]

    for move in moves:
        dir = move[0]
        n_steps = int(move[1])
        print(f"Move {n_steps} to {dir}")
        for _ in range(n_steps):
            if dir == "L":
                head.x -= 1
            elif dir == "R":
                head.x += 1
            elif dir == "U":
                head.y += 1
            elif dir == "D":
                head.y -= 1
            if pt == 1:
                t1 = adjust_tail(head, t1)
                tail_positions.append((t1.x, t1.y))
            elif pt == 2:
                t1 = adjust_tail(head, t1)
                t2 = adjust_tail(t1, t2)
                t3 = adjust_tail(t2, t3)
                t4 = adjust_tail(t3, t4)
                t5 = adjust_tail(t4, t5)
                t6 = adjust_tail(t5, t6)
                t7 = adjust_tail(t6, t7)
                t8 = adjust_tail(t7, t8)
                t9 = adjust_tail(t8, t9)
                tail_positions.append((t9.x, t9.y))

    distinct_positions_tail = set(tail_positions)
    return len(distinct_positions_tail)


pt1 = solve(1)
pt2 = solve(2)
print("Part1:", pt1)
print("Part2:", pt2)
