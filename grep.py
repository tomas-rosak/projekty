import sys

prikaz = sys.argv[1:]
try:       
    with open(prikaz[1]) as text:
        text = text.read()
    text = text.split("\n")
    pocet = 0
    for i in text:
        if prikaz[0] in i:
            if len(prikaz) == 3 and prikaz[-1] == "-c":
                print(i)
            pocet += 1  
    print("Slovo", prikaz[0], "se v textu nachazi", pocet)
except:
    print("Chyba")
