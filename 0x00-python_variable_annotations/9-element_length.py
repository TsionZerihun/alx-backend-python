#!/usr/bin/env python3
"""
Element length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    list
    """
    return [(i, len(i)) for i in lst]
