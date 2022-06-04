#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string
    ...
    Parameters
    ----------

    my_string : str
        The string to remove 'Cc' from

    Return:
        The new string
    """


    my_string_without_c = [j for j in my_string if j!= "c" and j !="C"]

    return ("".join(my_string_without_c))
