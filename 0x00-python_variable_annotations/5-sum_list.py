#!/usr/bin/env python3

"""sum_list module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of float"""
    return float(sum(map(lambda a: a, input_list)))
