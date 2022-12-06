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
print(sum_[-3:])
print(sum(sum_[-3:]))
