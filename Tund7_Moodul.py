def arithmetic(A: float, B: float, action: str) -> any:
    """ Simple calculator
    + - addition
    - - subtraction
    * - multiplication
    / - division
    :param (float) A: input from the user
    :param (float) B: input from the user
    :param (str) aciton: arithmetic operation that the user chooses
    :rtype: Any type(float or str)
    """

    if action in ["+", "-", "*", "/"]:
        if A == 0 and action == "/":
            return "DIV/0"
        else:
            return eval(str(A)+action+str(B))

    return "Unknown action"

def is_year_leap(year: int) -> bool:
    return year % 4 == 0

def square(side: float) -> any:
    """
    Returns perimeter of a square, area of ​​a square and diagonal of a square.
    """

    P = side * 4
    S = side ** 2
    D = (2)**(1/2)*side

    return P, S, D

def square_list(side: float) -> list:
    """
    Returns perimeter of a square, area of ​​a square and diagonal of a square AS LIST.
    """

    P = side * 4
    S = side ** 2
    D = (2)**(1/2)*side

    return list(P, S, D)

def season(month: int) -> str:
    pass