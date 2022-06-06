#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list
    ...
    Parameters
    ----------
    my_list : list
        The list to treat
    Return:
        An integer that is the biggest integer of the list
    """

    if len(my_list) == 0:
        return (None)
    elif len(my_list) == 1:
        return (my_list[0])
    else:
        for i in range(0, len(my_list)-1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 
        return (my_list[i + 1])
