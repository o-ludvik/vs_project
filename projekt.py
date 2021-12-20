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
#dictionary morseovy abecedy
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
special_char = [",",":","!","?","(",")"]

#Zašifrovává text do morzeovy abecedy
def ToMorse(text,preklad = ""):
    for char in text.lower():
        if char in Morseovka:
            preklad = preklad + Morseovka[char] + "/"
        elif char in special_char:
            preklad = preklad + char + "/"
        else:
            preklad = preklad + char
    return preklad + "//"


#Rozšifrovává kód z morzeovy abecedy 
def FromMorse(text):
  cords = [-1] + [i for i in range(len(text)) if text[i] == "/"]
  sl = [text[cords[i] + 1: cords[i + 1]] for i in range(len(cords) - 1)] + [""]
  dot = [i for i in range(len(sl) - 2) if sl[i] + sl[i + 1] + sl[i + 2] == ""]
  return "".join([inv_Morseovka[sl[i]] if not i in dot else "." for i in range(len(sl))])


zkama, jak = "0","0"
while zkama not in ["1","2"]:
    zkama = input("přeložit ze souboru(1) nebo z terminálu(2)?\n")
if zkama == "1":
    morse_file = open("morse.txt","r")
    morse = morse_file.read()
    morse_file.close()
    if morse[0] == "1":
        print(FromMorse(morse))
    elif morse[0] == "2":
        print(ToMorse(morse))
    else:
        print("přepiš morse.txt první charakter 1/2 => morseovka na abecedu(1), abeceda na morseovku(2)")
elif zkama == "2":
    while jak not in ["1","2"]:
        jak = input("morseovka na abecedu(1), abeceda na morseovku(2)?\n")
    if jak =="1":
        text = input("napiš morseovku ve formátu .../---/...// (/ = konec písmena, // = konec slova, /// = konec věty\n ")
        print(FromMorse(text))
    elif jak =="2":
        text = input("napiš text(mezery jenom mezi slovy): ")
        print(ToMorse(text))
else:
    print("špatný imput")
