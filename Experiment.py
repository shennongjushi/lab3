"""
Experiment
"""
import sys
def largest(my_list):
    """
    largest
    """
    if len(my_list) == 0:
        raise ValueError("Cannot call largest on empty list")
    my_max = -sys.maxint # "smallest" possible int
    # max = 0
    for index in range(len(my_list)):
        if (my_list[index] > my_max):
            my_max = my_list[index]
    return my_max
