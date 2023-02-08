#!/usr/bin/env python3
"""
sum list function
"""


def sum_list(input_list: list[float]):
    sum: float = 0
    for i in input_list:
        sum += i
        """
        return sum of lists as float
        """
    return sum
