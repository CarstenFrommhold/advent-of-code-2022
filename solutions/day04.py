import utils

data = utils.day_puzzle_to_list("04")


def elf_to_range(range_: str) -> list:
    start, stop = range_.split("-")
    return [x for x in range(int(start), int(stop) + 1)]


def check_if_included(r1: list, r2: list) -> bool:
    return all(r in r2 for r in r1) or all(r in r1 for r in r2)


def check_if_not_disjoint(r1: list, r2:list) -> bool:
    return any(r in r2 for r in r1) or any(r in r1 for r in r2)


def solve(pt: int):
    to_be_summed = []
    for elf_pair in data:
        print(elf_pair)
        elf1, elf2 = elf_pair.split(",")
        elf1_r = elf_to_range(elf1)
        elf2_r = elf_to_range(elf2)
        if pt == 1:
            c = check_if_included(elf1_r, elf2_r)  # Pt One
        elif pt == 2:
            c = check_if_not_disjoint(elf1_r, elf2_r)  # Pt Two
        to_be_summed.append(c)
    return sum(to_be_summed)


pt1 = solve(1)
pt2 = solve(2)
print("Part1:", pt1)
print("Part2:", pt2)
