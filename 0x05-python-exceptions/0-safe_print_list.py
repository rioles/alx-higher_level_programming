#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ prints x elements of a list.
    Args:
        x (int): The number of element to print.
        my_list (list): The list of element to print
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    real_number_of_element_return = 0

    for i in range(0, x):
        try:
            print(f"{my_list[i]}", end="")
            real_number_of_element_return += 1
        except IndexError:
            break
    print("")
    return real_number_of_element_return
