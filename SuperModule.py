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

def read_file(file: str) -> list:
    f = open(file, 'r', encoding="utf-8-sig")
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
    return lines

def print_file(file: str):
    for line in read_file(file):
        print(line)

def write_file(file: str, lines:list):
    f = open(file, 'w', encoding="utf-8-sig")
    for line in lines:
        f.write(line + '\n')
    f.close()