"""safely_get_value module"""

from typing import Any, Dict


def safely_get_value(dct: Dict, key: Any, default: Any = None) -> Any:
    """Return the value in the dictionary specified the key"""
    if key in dct:
        return dct[key]
    else:
        return default
