"""
Écrire l’algorithme qui effectue un cryptage de Vigenère, en demandant au départ la clé à l’utilisateur.
Phrase à tester : il faut coder cette phrase
Cle à tester : VIGENERE
"""

lettres = "abcdefghijklmnopqrstuvwxyz"
lettres = lettres.upper()


def menu() -> [str]:
    """
    Le menu d'application.
    """
    print()
    print('  #########################CRYPTO-VIGENERE########################################### ')
    print('Le program permettre d\'encoder un text par la methode VIGENERE.')
    print('L\'alphabet utilise c\'est "abcdefghijklmnopqrstuvwxyz".')
    print('La cryptogramme vous sera renvoyer en majuscules.')
    print()
    return str


def choix() -> bool:
    """
    Verifie si la choix d'utilisateur est valide. 1 pour l'encodage et 2 pour le decodage.
    input: var util. type int
    output: bool
    """

    if util == 1 or 2:
        return True
    else:
        return False


def encodage(string) -> [str]:
    """
    Utiliser deux listes pour sauver l'index des lettres de la phrase et de la clé introduisaient
    par l'utilisateur mais en rapport avec le dictionnaire utilise (sauf les espaces libres).
    L'index des lettres de la phrase est decale par l'index des lettres de la cle.
    input: string
    output: string
    """

    cle_indx = []  # ajouter l'index des lettres de la cle
    for i in cle:
        if i in lettres:
            cle_indx.append(lettres.index(i))

    phr_pl_index = []  # ajouter l'index des lettres de la phrase
    j = 0  # variable utilise pour accéder les valeurs de la liste cle_index.
    for i in phrase:  # ajouter les espaces vides a la liste mais sans codage.
        if i == " ":
            i = i
            phr_pl_index.append(i)

        elif i in lettres:  # decalage des lettres de la text encode
            i = lettres[(lettres.index(i) + cle_indx[(j % len(cle_indx))]) % len(lettres)]
            j += 1  # l'index de la cle_indx est ajusté par le % de sa longueur pour
            phr_pl_index.append(i)  # garantir le retour a l'index 0 quand j > que l'index du cle_indx

    phrasencode = "".join(phr_pl_index)  # les lettres encodent sont ajouter dans un string.

    return phrasencode


def decodage(string) -> [str]:
    """
    Le decodage est identique a la function d'encodage ( def encodage() ) avec la seule difference que les valeures
    de la variable cle_indx sont substitue de la phr_pl_index.
    """
    cle_indx = []
    for i in cle:
        if i in lettres:
            cle_indx.append(lettres.index(i))

    phr_pl_index = []
    j = 0
    for i in phrase:
        if i == " ":
            i = i
            phr_pl_index.append(i)

        elif i in lettres:  # l'index decale est substitue.
            i = lettres[(lettres.index(i) - cle_indx[(j % len(cle_indx))] + 26) % len(lettres)]
            j += 1
            phr_pl_index.append(i)

    phrasdecode = "".join(phr_pl_index)
    return phrasdecode


if __name__ == '__main__':

    menu()
    phrase = input('Votre phrase: ').upper()
    cle = input('Votre cle: ').upper()
    print('Choisissez le traitement a faire. Pour encodage appuyez sur 1 pour décodage sur 2. ')
    util = int(input('Votre choix: '))

    while choix is False:
        util = (input('Votre choix: '))
    if util == 1:
        print(encodage(phrase))
    else:
        print(decodage(phrase))
