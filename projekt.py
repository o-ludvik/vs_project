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
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "ch":"----",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
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
}

def FromMorse(text):
    return text

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
        print(FromMorse())
    elif jak =="2":
        text = input("napiš text: ")
        print(ToMorse())