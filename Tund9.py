TUNDTXT = "Tund9.txt"

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

names_list = ["Ann", "Kati", "Mari"]
write_file(TUNDTXT, names_list)

print_file(TUNDTXT)

with open(TUNDTXT, 'r', encoding="utf-8-sig") as f:
    print(f.read())

def file_to_dict(file: str):
    riik_pealinn = {}
    pealinn_riik = {}
    riigid = []
    for line in read_file(file):
        k,v = line.strip().split("-")
        riik_pealinn[k] = v
        pealinn_riik[v] = k
        riigid.append(k)

    return riik_pealinn, pealinn_riik, riigid

riik_pealinn, pealinn_riik, riigid = file_to_dict("riigid_pealinnad.txt")

for key, value in riik_pealinn.items():
    print(key, value)
    
print()

for key, value in pealinn_riik.items():
    print(key, value)

print()

for value in riigid:
    print(value)