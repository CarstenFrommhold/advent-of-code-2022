import utils

in_ = utils.day_puzzle_to_list("06")[0]
buffer = [c for c in in_]


def unique(list_) -> bool:
    return len(list_) == len(set(list_))


received = False

start, end = (0, 14)
while not received:
    if unique(buffer[start: end]):
        received = True
    else:
        start += 1
        end += 1

print(end)
