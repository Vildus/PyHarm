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
