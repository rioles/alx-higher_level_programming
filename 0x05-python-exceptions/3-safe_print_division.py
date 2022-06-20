def safe_print_division(a, b):
    """function that divides 2 integers and prints the result.


    Args:
        a (int): dividend
        b (int): divisor

    Return:
        The result of division
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
