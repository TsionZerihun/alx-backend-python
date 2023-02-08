#!/usr/bin/env python3
"""
tokv function
"""
from typing import Tuple, Union


def to_kv(k: str,v: Union[int, float]) -> Tuple[str, float]:
    """
    return tuple
    """
    return(k, v**2)
