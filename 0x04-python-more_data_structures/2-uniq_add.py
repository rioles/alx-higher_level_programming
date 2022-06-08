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
    unique_value = {}
    for i in my_list:
        if i in unique_value:
            continue
        unique_value[i] = True
    return sum(unique_value)
