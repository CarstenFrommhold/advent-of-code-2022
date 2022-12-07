import utils

data = utils.day_puzzle_to_list("01")

elfs = []
elf = []
for entry in data:
    if entry != "":
        elf.append(float(entry))
    else:
        elfs.append(elf)
        elf = []

sum_ = [sum(elf) for elf in elfs]
sum_.sort()
pt1 = sum_[-3:]
pt2 = sum(sum_[-3:])

print("Part1:", pt1)
print("Part2:", pt2)
