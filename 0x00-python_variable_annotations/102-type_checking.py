# Import the necessary typing modules
#!/usr/bin/python3
from typing import Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """ Create a new tuple called zoomed_in using a list comprehension"""
    zoomed_in: Tuple = tuple(
        item for item in lst
        for i in range(factor)
    )
    # Return the zoomed_in tuple
    return zoomed_in


# Create a tuple called array with some initial values
array: Tuple = (12, 72, 91)

# Call the zoom_array function with the default factor (2)
zoom_2x = zoom_array(array)

# Call the zoom_array function with a factor of 3
zoom_3x = zoom_array(array, 3)
