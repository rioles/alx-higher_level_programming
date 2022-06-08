def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new list
    ...
    Parameters
    ----------
    my_list : list
        The list to treat
    search : integer
        The element to replace in the list
    replace : integer
        The new element to replace
    Return:
        New list with replacement to the element
        to replace in the list with the new element
        
    """

    return list(map(lambda x : replace if x == search else x, my_list))


