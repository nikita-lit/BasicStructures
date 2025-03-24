# --------------------------------------

import random

# --------------------------------------

USER_NAME = 0
USER_PSW = 1
USER_RIGHTS = 2

def get_input(data_type: type, text: str) -> any:
    """
    Возрощает данные из input с определенным типом даннных.
    :param (Type) data_type: тип данных.
    :param (str) text: текст который выводится пользователю.
    """

    try:
        data = data_type(input(text))
    except:
        return False

    return data

def generate_password() -> str:
    """
    Generates password using random.
    """

    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()

    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword

def is_password_valid(password) -> bool:
    alpha = 0
    num = 0
    for char in password:
        if char.isalpha():
            alpha += 1
        elif char.isnumeric():
            num += 1

    if alpha == 0 and num == 0:
        print("Parool ei sisalda vähemalt numbreid või tähti!")
        return False

    if len(password) < 5:
        print("Parool on liiga väike. Vähemalt 5 tähemärki!")
        return False

    return True

def is_user_name_valid(user_name) -> bool:
    if user_name.isnumeric():
        print("Nimi ei saa koosneda ainult numbritest.")
        return False

    if len(user_name) < 3:
        print("Nimi on liiga väike. Vähemalt 3 tähemärki!")
        return False

    return True

def is_admin(user):
    if "admin" in user[USER_RIGHTS]:
        return True

    return False