# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import re

# Press the green button in the gutter to run the script.
if __name__ == '__test__':
    print_hi('PyCharm')
    texte = "AF007 BA984 LH7790 AA381 KL976 AF909"
    motif_A = r"[A-Z]{2}[0-9]+"
    motif_B = r'[A-Z]{2}[0-9]*9[0-9]*'  # recherche de numéro de vol avec un '9’…
    resultat_match = re.match(motif_A, texte)
    if resultat_match:
        print(f"Fonction match : {resultat_match.group()}")
    else:
        print(f"Fonction match : {resultat_match}")
    resultat_search = re.match(motif_B, texte)
    if resultat_search:
        print(f"Fonction search : {resultat_search.group()}")
    else:
        print(f"Fonction search : {resultat_search}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
