#!/usr/bin/env python3
"""zoom_array module"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Create and return a new list called
        zoomed_in using a list comprehension"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]

    return zoomed_in


array: Tuple = (12, 72, 91)

# Call the zoom_array function with the default factor (2)
zoom_2x = zoom_array(array)

# Call the zoom_array function with a factor of 3
zoom_3x = zoom_array(array, 3)
