import string
import numpy as np
import utils


data = utils.day_puzzle_to_list("03")


def get_priority(letter: str) -> int:
    if letter.islower():
        return string.ascii_lowercase.index(letter) + 1
    else:
        return string.ascii_uppercase.index(letter) + 27


to_be_summed = []
for rucksack in data:
    l = len(rucksack)
    compartment_1, compartment_2 = (rucksack[:int(l/2)], rucksack[int(l/2):])
    shared = set([x for x in compartment_1 if x in compartment_2])
    shared = next(iter(shared))
    to_be_summed.append(get_priority(shared))

pt1 = sum(to_be_summed)


# Pt Two
to_be_summed = []
for elf_group in np.array_split(data, len(data)/3):
    g1, g2, g3 = elf_group
    shared = set([x for x in g1 if (x in g2 and x in g3)])
    shared = next(iter(shared))
    to_be_summed.append(get_priority(shared))

pt2 = sum(to_be_summed)

print("Part1:", pt1)
print("Part2:", pt2)
