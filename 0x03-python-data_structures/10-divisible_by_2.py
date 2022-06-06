def divisible_by_2(my_list=[]):
    result = [ False for i in my_list ]
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            result[i] = True     
    return result
