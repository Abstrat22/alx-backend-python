#!/usr/bin/env python3

"""make_multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a fuction that multiplies a float by 'multiplier' """
    return lambda a: a * multiplier
