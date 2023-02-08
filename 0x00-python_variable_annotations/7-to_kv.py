##!/usr/bin/env python3
"""
tokv function
"""
from typing import List, Union


def to_kv(k: str,v: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    return tuple
    """
    return(k,v)


print(to_kv("eggs", 3))
print(to_kv("school", 0.02))