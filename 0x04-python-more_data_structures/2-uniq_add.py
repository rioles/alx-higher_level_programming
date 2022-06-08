#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    a function that adds all unique integers in a list
    (only once for each integer).
    ...
    Parameters
    ----------
    my_list : list
        The list to sum
    Return:
        The sum of all unique integer in a list
    """
    return sum(set(my_list))
