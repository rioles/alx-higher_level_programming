#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print a list of integers
    ...
    Parameters
    ----------
    my_list : list optional
        The list of integers
    Return:
        None
    """

    for i in range(0,len(my_list)):
        print(f"{my_list[i]}")
