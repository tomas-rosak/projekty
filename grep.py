#!/usr/bin/env python3
import sys

prikaz = sys.argv[1:]
if len(prikaz) < 2:
    print("Malo argumentu")
    exit(1)
try:
    with open(prikaz[1]) as text:
        text = text.read()
except:
    print("Nespravna cesta")
    exit(1)
text = text.split("\n")
pocet = 0
for i in text:
    if prikaz[0] in i:
        if len(prikaz) == 2:
            print(i)
        pocet += 1 
if len(prikaz) == 3 and prikaz[-1] == "-c":
    print(pocet)
