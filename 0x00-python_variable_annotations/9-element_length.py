#!/usr/bin/env python3

"""element_length module"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of a sequence of elements and their length"""
    return [(i, len(i)) for i in lst]