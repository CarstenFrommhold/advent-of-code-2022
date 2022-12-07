import utils

in_ = utils.day_puzzle_to_list("06")[0]
buffer = [c for c in in_]


def unique(list_) -> bool:
    return len(list_) == len(set(list_))


def solve(end_: int):
    received = False
    start, end = (0, end_)
    while not received:
        if unique(buffer[start: end]):
            received = True
        else:
            start += 1
            end += 1
    return end


pt1 = solve(4)
pt2 = solve(14)
print("Part1:", pt1)
print("Part2:", pt2)
