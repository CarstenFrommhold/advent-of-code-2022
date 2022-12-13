""" utils for advent of code 22"""
from typing import Callable


def day_puzzle_to_list(day: str, sep="xxx") -> list:
    with open(f"../puzzles/day{day}.txt", "r") as f:
        data = f.read().replace('\n', sep).split(sep)
    return data


def bubble_sort(array, sort_function: Callable):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if not sort_function(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array