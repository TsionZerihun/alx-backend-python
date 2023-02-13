#!/usr/bin/env python3
"""
duck-typed annotation
"""


def safe_first_element(lst):
    try:
        return lst[0]
    except TypeError as e:
        print(e)