"""
This module contains two useful functions from statistics: mean and median.

Note however, that these two functions both crash if the list of numbers is empty.

If we really wanted to use this module in out programs, we should improve the functions so that they don't crash"""

def mean(numbers):
    sum = 0
    size = len(numbers)
    for n in numbers:
        sum = sum + n
    return sum /size

def median(numbers):
    numbers = sorted(numbers)
    size = len(numbers)
    mid = size // 2
    if size % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid -1] + numbers[mid]) / 2