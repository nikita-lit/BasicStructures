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