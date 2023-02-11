##!/usr/bin/env python3
"""
make element length
"""
from  typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence,int]]:
    """
    Returns list
    """
    return [(i, len(i)) for i in lst]