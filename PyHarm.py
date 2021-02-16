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
            elif kvalita == "dim":
                self.quality = "dim"
            elif kvalita == "+" or kvalita == "aug":
                self.quality = "Aug"
            elif kvalita == "7":
                self.quality = "Dom7"
            elif kvalita == "maj7":
                self.quality = "Maj7"
            else:
                varuj(" Akordová značka " + kvalita + " neexistuje. Bude Automaticky dur")
                self.quality = "Major"
        self.value = to_num(self.root)

    def __repr__(self):
        return self.root + self.quality
    
    def chord(self):
        k = self.quality
        rr = to_note(self.value)
        if k == "Major":
            return rr
        elif k == "minor":
            return rr + "m"
        elif k == "dim":
            return rr + "dim"
        else:
            return "BROKEN_AKORD_ERROR"


class Scale:
    def __init__(self, root, typ):
        self.tony_num = []
        self.tony = []
        self.typ = typ
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
    def akordy(self):
        out = []
        if self.typ == "Major":
            ends = ["", "m", "m", "", "", "m", "dim"]
        else:
            ends = ["m", "dim", "", "m", "m", "", ""]
        for i in range(7):
            out.append(self.tony[i]+ends[i])
        return out

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

def to_roman(num, typ):
    if num == 1:
        roman = "i"
    elif num == 2:
        roman = "ii"
    elif num == 3:
        roman = "iii"
    elif num == 4:
        roman = "iv"
    elif num == 5:
        roman = "v"
    elif num == 6:
        roman = "vi"
    elif num == 7:
        roman = "vii"
    if typ == "Major":
        roman = roman.upper()
    if typ == "dim":
        roman += "°"
    if typ == "Dom7":
        roman = roman.upper() + "7"
    return roman


def analyse(para):
    akordy = []
    out = ""
    for i in para:
        akordy.append(Akord(i))
    first = akordy[0]
    stupnice = Scale(first.root, first.quality)
    legal = stupnice.akordy()
    for akord in akordy:
        if not akord.chord() in legal:
            out += akord.chord() + "? "
        else:
            out += to_roman((legal.index(akord.chord()) + 1), akord.quality) + " "
    print(out)


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
