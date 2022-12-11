import utils
from dataclasses import dataclass
import math
from typing import Callable

data = utils.day_puzzle_to_list("11")
chunks = [data[x:x+7] for x in range(0, len(data), 7)]


@dataclass
class Item:
    worry_level: int


@dataclass
class Monkey:
    items: list
    operation: Callable
    test_div: int
    test_true: int
    test_false: int
    inspect_items_counter: int = 0


monkeys = {}


def throw_to(worry_level: int, divisible_by: int, monkey_to_true: int, monkey_to_false: int) -> int:
    if worry_level % divisible_by == 0:
        return monkey_to_true
    else:
        return monkey_to_false

# ['Monkey 0:', '  Starting items: 54, 53', '  Operation: new = old * 3', '  Test: divisible by 2', '    If true: throw to monkey 2', '    If false: throw to monkey 6', '']


for monkey_no, chunk in enumerate(chunks):
    for no, row in enumerate(chunk):
        if no == 1:
            start_items = eval(row.replace("  Starting items: ", ""))
            if isinstance(start_items, int):
                start_items = [start_items]
            items = [Item(worry_level) for worry_level in start_items]
        elif no == 2:
            operation = row.replace("  Operation: new ", "lambda x: ").replace("= old", "x").replace(" old", "x")
            operation = eval(operation)
        elif no == 3:
            test_div = eval(row.replace("  Test: divisible by ", ""))
        elif no == 4:
            test_true = eval(row.replace("    If true: throw to monkey ", ""))
        elif no == 5:
            test_false = eval(row.replace("    If false: throw to monkey ", ""))
    monkeys[monkey_no] = Monkey(items, operation, test_div, test_true, test_false)

print(monkeys)

for round in range(1, 21):
    for monkey_no, monkey in monkeys.items():
        while monkey.items != list():  # don't iterate over mutable when you change it.
            item = monkey.items.pop(0)  # take first item
            worry_level = item.worry_level
            worry_level = monkey.operation(worry_level)
            # Monkey gets bored
            worry_level = math.floor(worry_level/3)
            # Throw to another monkey
            throw_to_monkey = throw_to(worry_level, monkey.test_div, monkey.test_true, monkey.test_false)
            monkeys[throw_to_monkey].items.append(Item(worry_level))
            monkey.inspect_items_counter += 1


counters = []
for monkey in monkeys.values():
    counters.append(monkey.inspect_items_counter)
counters.sort()
pt1 = counters[-1] * counters[-2]
print(pt1)
