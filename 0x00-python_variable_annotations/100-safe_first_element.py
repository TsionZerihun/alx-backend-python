#!/usr/bin/env python3
"""
duck-typed annotation
"""
from typing import List


def safe_first_element(lst: List) -> int:
    try:
        return lst[0]
    except TypeError as e:
        print(e)
