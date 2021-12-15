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
    "á":".-",
    "a":".-",
    "b":"-...",
    "č":"-.-.",
    "c":"-.-.",
    "ď":"-..",
    "d":"-..",
    "ě":".",
    "é":".",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "ch":"----",
    "í":"..",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "ň":"-.",
    "n":"-.",
    "ó":"---",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "ř":".-.",
    "r":".-.",
    "š":"...",
    "s":"...",
    "ť":"-",
    "t":"-",
    "ú":"..-",
    "ů":"..-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "ý":"-.--",
    "y":"-.--",
    "ž":"--..",
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
    " ":"",
    ".":"/"
}
inv_Morseovka = {v: k for k, v in Morseovka.items()}

def ToMorse(text,preklad = ""):
    for char in text.lower():
        if char in Morseovka:
            preklad = preklad + Morseovka[char] + "/"
        else:
            preklad = preklad + char
    return preklad
#udělat aby před : atd. nebylo /


def FromMorse(text):
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