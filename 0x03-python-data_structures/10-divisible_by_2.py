#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list
    ...
    Parameters
    ----------
    my_list : list
        The list to check
    Return:
        A new list with True or False, depending
         on whether the integer at the same position
         in the original list is a multiple of 2
    """


    result = [ False for i in my_list ]
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            result[i] = True

    return (result)
