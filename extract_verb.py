import re

if __name__ == '__TD__':
    with open("verb.txt", "r", encoding="utf-8") as f:
        contenu = f.read()

    motif_A = r"^[a-zA-Z]+"
    resultat = re.findall(motif_A, contenu, re.MULTILINE) #  multiline sert à liste sur une chaine de caractère dit à plusieur ligne
    print(resultat)