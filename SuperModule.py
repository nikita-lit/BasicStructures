import time

def get_input(data_type: type, text: str) -> any:
    """
    Tagastab määratud andmetüübiga sisendi andmed.
    :param (tüüp) data_type: andmetüüp.
    :param (str) tekst: kasutajale kuvatav tekst.
    """

    try:
        data = data_type(input(text))
    except:
        return False

    return data