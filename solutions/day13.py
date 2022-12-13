import utils

data = utils.day_puzzle_to_list("13")

chunks = [data[x:x+3] for x in range(0, len(data), 3)]
pairs = [(eval(x[0]), eval(x[1])) for x in chunks]


def inputs_in_right_order(left, right) -> bool:
    if isinstance(left, list) and isinstance(right, int):
        sub = inputs_in_right_order(left, [right])
        if sub is not None:
            return sub
    if isinstance(left, int) and isinstance(right, list):
        sub = inputs_in_right_order([left], right)
        print(sub)
        if sub is not None:
            return sub
    if left == [] and right == []:
        return None
    if not left and right:
        return True  # Left sight ran out of items
    for no, entry in enumerate(left):
        if len(right) < no + 1:
            return False   # Right side ran out of items
        if isinstance(entry, int) and isinstance(right[no], list):
            sub = inputs_in_right_order([entry], right[no])
            if sub is not None:
                return sub
        if isinstance(entry, list) and isinstance(right[no], int):
            sub = inputs_in_right_order(entry, [right[no]])
            if sub is not None:
                return sub
        if isinstance(entry, list):
            sub = inputs_in_right_order(entry, right[no])
            if sub is not None:
                return sub
        if entry < right[no]:
            return True   # Left side is smaller
        if entry > right[no]:
            return False  # Right side is smaller
    return True


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


print("Part 1:", pt1)
print("Part 2:", pt2)
