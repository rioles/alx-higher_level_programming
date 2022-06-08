def uniq_add(my_list=[]):
    
    unique_value = {}

    for i in my_list:
        if i in unique_value:
            continue
        unique_value[i] = True
    return sum(unique_value)
