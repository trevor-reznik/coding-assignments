"""Create array which corresponds with given reference diagram.

Author: Christian P. Byrne
Course: CSC120 Summer 2021
"""

import list_node


def grid_of_arrays():
    """Create grid of arrays with references corresponding to 
    a diagram.

    Returns:
        array
    
    
    """
    nine = [None, (2,2), None]
    eight = [nine, (1,2), None]
    seven = [eight, (0,2), None]
    six = [None, (2,1), nine]
    five = [six, (1,1), eight]
    four = [five, (0,1), seven]
    three = [None, (2,0), six]
    two = [three, (1,0), five]
    return [two, (0,0), four]