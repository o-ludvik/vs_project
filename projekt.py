#Morseovka
#Oliver Ludvík, Ondřej Sedláček, Martin Sedláček

"""
Vytvořte program, který umí kódovat i dekódovat Morseovu abecedu.
VSTUP
• Textový řetězec v uvozovkách
• Bude čistě na řešitelském týmu, aby vymyslelo vhodný způsob zadávání vstupu.
VÝSTUP
• Zakódovaná, případně dekódovaná morseovka
"""

Morseovka = {
    "a":".-",
    "á":".-",
    "b":"-...",
    "c":"-.-.",
    "č":"-.-.",
    "d":"-..",
    "ď":"-..",
    "e":".",
    "é":".",
    "ě":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "ch":"----",
    "i":"..",
    "í":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "ň":"-.",
    "o":"---",
    "ó":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "ř":".-.",
    "s":"...",
    "š":"...",
    "t":"-",
    "ť":"-",
    "u":"..-",
    "ů":"..-",
    "ú":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "ý":"-.--",
    "z":"--..",
    "ž":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    " ":"",
    ".":"/"
}

def FromMorse(text,preklad = ""):
    for char in text.lower():
        if char in Morseovka:
            preklad = preklad + Morseovka[char] + "/"
        else:
            preklad = preklad + char + "/"
    return preklad
#udělat aby před : atd. nebylo /


def ToMorse(text):
    return text

zkama = input("přeložit ze souboru? y/n: ").lower()
if zkama == "y":
    morse_file = open("morse.txt","r")
    morse = morse_file.read()
    morse_file.close()
else:
    jak = input("1 pokud z morseovky do abeceny, 2 pokud naopak: ")
    if jak =="1":
        text = input("napiš morseovku: ")
        print(FromMorse(text))
    elif jak =="2":
        text = input("napiš text: ")
        print(ToMorse(text))