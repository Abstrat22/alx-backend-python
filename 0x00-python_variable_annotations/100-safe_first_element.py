"""safe_first_element module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the value at index 0 of the passed sequence or None for None types"""
    if lst:
        return lst[0]
    else:
        return None
