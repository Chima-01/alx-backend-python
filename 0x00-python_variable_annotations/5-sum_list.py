#!/usr/bin/env python3
"""
    type-annotated function sum_list which takes
    a list input_list of floats as argument
    returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Args: type list of float
    """
    total: float = 0
    for i in range(0, len(input_list)):
        total += input_list[i]
    return total
