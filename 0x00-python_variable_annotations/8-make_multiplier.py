#!/usr/bin/env python3
"""
callable function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function
    """
    def fun(number: float) -> float:
        """
        multiplies a number with float
        """
        return number * multiplier

    return fun
