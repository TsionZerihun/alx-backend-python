#!/usr/bin/env python3
"""
    sum list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Args:
            input_list: float numbers
            
        Return:
            Sum of the float numbers
    """
    
    sum: float = 0
        
    for i in input_list:
        sum += i
        
    return sum
