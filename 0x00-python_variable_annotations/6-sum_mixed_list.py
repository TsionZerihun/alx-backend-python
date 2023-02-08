##!/usr/bin/env python3
"""
sum mexed list
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int,float]]) -> float:
    """
    Returns sum of lists
    """

    return sum(mxd_lst)


mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans)