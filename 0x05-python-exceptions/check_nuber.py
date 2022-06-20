def check_if_number_is_integer(value):
    """a function that check if number is integer
    Args:
        value (string): value to print
    Returns:
        True if value is integer otherwise False
    """

    string_value = str(value)
    integer_numbers = {'0','1','2','3','4','5','6','7','8','9'}
    
    if string_value[0] == "-" or string_value[0] == "+":
        counter = 1
    else:
        counter = 0

    for counter in range(counter,len(string_value)):
        if string_value[counter] not in number_array:
            return False
    return True



if __name__ == "__main__":
   print(safe_print_integer("okay"))
   print(safe_print_integer(80))
   print(safe_print_integer(-100))
   print(safe_print_integer("1234p"))
   print(safe_print_integer("12-78"))

