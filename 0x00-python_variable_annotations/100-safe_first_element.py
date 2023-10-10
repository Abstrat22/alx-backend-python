"""safe_first_element module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the value at first index of the passed sequence"""
    if lst:
        return lst[0]
    else:
        return None
