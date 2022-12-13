import utils

data = utils.day_puzzle_to_list("13")

chunks = [data[x:x+3] for x in range(0, len(data), 3)]
pairs = [(eval(x[0]), eval(x[1])) for x in chunks]


def inputs_in_right_order(left, right):
    min_ = min(len(left), len(right))
    for i in range(min_):
        left_item, right_item = left[i], right[i]
        if isinstance(left_item, int) and isinstance(right_item, int):
            if left_item == right_item:
                continue
            return left_item < right_item
        elif isinstance(left_item, int) or isinstance(right_item, int):
            if isinstance(left_item, int):
                sub = inputs_in_right_order([left_item], right_item)
            else:
                sub = inputs_in_right_order(left_item, [right_item])
            if sub is None:
                continue
            return sub
        else:
            sub = inputs_in_right_order(left_item, right_item)
            if sub is None:
                continue
            return sub

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False


# Pt 1
to_be_summed = 0
for no, pair in enumerate(pairs, 1):
    if inputs_in_right_order(pair[0], pair[1]):
        to_be_summed += no
pt1 = to_be_summed


# Pt 2
pairs.append(([[2]], [[6]]))
packets = []
for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])

p_sorted = utils.bubble_sort(packets, inputs_in_right_order)
pt2 = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


print("Part 1:", pt1)  # soll 5198
print("Part 2:", pt2)  # soll 22344
