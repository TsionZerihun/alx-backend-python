#!/usr/bin/env python3
"""
duck-typed annotation
"""
from typing import List, Union


def safe_first_element(lst: List) -> Union[Any, None]:
    """
    Return first Element
    """
    try:
        return lst[0]
    except TypeError as e:
        print(e)
