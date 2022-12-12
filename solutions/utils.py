""" utils for advent of code 22"""


def day_puzzle_to_list(day: str, sep="xxx") -> list:
    with open(f"../puzzles/day{day}.txt", "r") as f:
        data = f.read().replace('\n', sep).split(sep)
    return data
