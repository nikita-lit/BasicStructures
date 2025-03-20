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
    Returns perimeter, area and diagonal of a square.
    Tagastab ruudu perimeetri, pindala ja diagonaali.
    """

    P = side * 4
    S = side ** 2
    D = (2)**(1/2)*side

    return P, S, D

def square_list(side: float) -> list:
    """
    Returns perimeter, area and diagonal of a square AS LIST.
    Tagastab ruudu perimeetri, pindala ja diagonaali.
    """

    P = side * 4
    S = side ** 2
    D = (2)**(1/2)*side

    return list(P, S, D)

def season(month: int) -> str:
    """
    Tagastab kuu nime numbri järgi.
    Returns the month name by number.
    """

    if month in [1, 2, 12]:
        return "talv"
    elif month in [9, 10, 11]:
        return "sügis"
    elif month in [6, 7, 8]:
        return "suvi"
    elif month in [3, 4, 5]:
        return "kevad"

    return "Tundmatu kuu"

def bank(a: float, years: int) -> float:
    """
    Tagastab deposiidi suuruse aastate pärast.
    Returns the size of the deposit after years.
    """

    return (a * 1.1) ** years

def is_prime(number: int) -> bool:
    """
    Tagastab kas antud arv on algarv.
    Returns if the given number is prime.
    """

    if number >= 0 and number <= 1000:
        d = 2
        while d * d <= number and number % d != 0:
            d += 1

        return d * d > number
    else:
        return False

def date(day: int, month: int, year: int) -> bool:
    """
    Tagastab kas antud kuupäev on olemas.
    Returns if the given date is valid.
    """

    if month in [1,3,5,7,8,10,12]:
        return day >= 1 and day <= 31
    elif month in [4,6,9,11]:
        return day >= 1 and day <= 30
    elif month == 2:
        if is_year_leap(year):
            return day >= 1 and day <= 29
        else:
            return day >= 1 and day <= 28

    return False

# ord - возрощает номер символа в Unicode
# chr - возрощает символ по номеру в Unicode

def XOR_cipher(plaintext, key):
    cipher_text = ""

    for i, char in enumerate(plaintext):
        char_code = ord(char)
        key_code = ord(key[i % len(key)])

        encrypted_code = char_code ^ key_code
        cipher_text += chr(encrypted_code)
        
    return cipher_text


def XOR_uncipher(ciphertext, key):
    text = ""

    for i, char in enumerate(ciphertext):
        char_code = ord(char)
        key_code = ord(key[i % len(key)])
        
        decrypted_code = char_code ^ key_code

        text += chr(decrypted_code)
        
    return text