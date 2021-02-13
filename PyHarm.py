class Akord:
    def __init__(self, chord):
        if len(chord) > 1:
            if chord[1] == "#" or chord[1] == "b":
                self.root = chord[0:2].capitalize()
                ton_len = 2
            else:
                self.root = chord[0].capitalize()
                ton_len = 1
        else:
            self.root = chord[0].capitalize()
            ton_len = 1
        if self.root not in ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "Hb", "B", "H"]:
            varuj(" Tón " + self.root + " neexistuje! Bude tedy C")
            self.root = "C"
        if len(chord) == ton_len:
            self.quality = "Major"
        else:
            kvalita = chord[ton_len:]
            if kvalita == "m":
                self.quality = "minor"
            elif kvalita == "M":
                self.quality = "Major"
            else:
                varuj(" Akordová značka " + kvalita + " neexistuje. Bude Automaticky dur")
                self.quality = "Major"
        self.value = to_num(self.root)

    def __repr__(self):
        return self.root + "_" + self.quality + "_" + str(self.value)


class Scale:
    def __init__(self, root, typ):
        self.tony_num = []
        self.tony = []
        if typ == "Major":
            offset = [2, 2, 1, 2, 2, 2]
        else:
            offset = [2, 1, 2, 2, 1, 2]
        val = to_num(root)
        self.tony_num.append(val)
        for i in range(len(offset)):
            val += offset[i]
            val %= 12
            self.tony_num.append(val)
        for num in self.tony_num:
            self.tony.append(to_note(num))

def varuj(text):
    print('\x1b[0;31;40m' + "[WARNING]" + '\x1b[0m' + text)


def to_num(ton):
    out = 0
    tony = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "Hb", "B", "H"]
    valu = [0,   1,    1,    2,   3,    3,    4,   5,   6,    6,    7,   8,    8,    9,    10,   10,  10,   11,  11 ]
    for i in range(len(tony)):
        if ton == tony[i]:
            out = valu[i]
    return out

def to_note(ton):
    tony = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
    return tony[ton]


def analyse(para):
    akordy = []
    for i in para:
        akordy.append(Akord(i))
    first = akordy[0]
    stupnice = Scale(first.root, first.quality)
    print(stupnice.tony)


def execute(inp):
    spl = inp.split()
    if len(spl) == 0:
        return 0
    com = spl[0]
    para = spl[1:]
    if com == "quit":
        return "term"
    elif com == "analyse":
        analyse(para)
    else:
        print("\nPříkaz " + com + " neexistuje!\nPro seznam příkazů použijte příkaz help")
    return 0


print("PyHarm ver. 1.0\n"
      "Analyzátor a generátor akordových postupů\n"
      "Pro seznam příkazů použijte příkaz help\n"
      "By VP 2021\n")

run = True
while run:
    try:
        inp = input("PyHarm>")
        ret = execute(inp)
        if ret == "term":
            run = False
    except KeyboardInterrupt:
        print("Pro ukončení programu je třeba použít příkaz quit")
    except:
        varuj("ERROR 1")
print("Program ukončen")
