import re

def validate(cnpj):
    sequence = cnpj[0] * len(cnpj)

    if sequence == cnpj:
        return False

def cnpjCleanFormat(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def calcFirstDig(cnpj):
    firstDig = 0
    total = 0
    reverse = 5
    while True:
        for value in cnpj:
            #print(f"{value} x {reverse}")
            total += int(value) * reverse
            reverse -= 1
            if reverse < 2:
                break

        reverse = 9

        cutCNPJ = cnpj[4:]
        for value in cutCNPJ:
            #print(f"{value} x {reverse}")
            total += int(value) * reverse
            reverse -= 1
            if reverse < 2:
                break
        break
    
    #print (total)
    aux = 11 - (total % 11)
    if aux < 9:
        firstDig = aux
    else:
        firstDig = 0

    return firstDig

def calcSecondDig(cnpj):
    secondDig = 0
    total = 0
    reverse = 6
    while True:
        for value in cnpj:
            #print(f"{value} x {reverse}")
            total += int(value) * reverse
            reverse -= 1
            if reverse < 2:
                break

        reverse = 9

        cutCNPJ = cnpj[5:]
        for value in cutCNPJ:
            #print(f"{value} x {reverse}")
            total += int(value) * reverse
            reverse -= 1
            if reverse < 2:
                break
        break
    
    #print (total)
    aux = 11 - (total % 11)
    if aux < 9:
        secondDig = aux
    else:
        secondDig = 0

    return secondDig

def verifyCNPJ(oldCNPJ, newCNPJ):
    if oldCNPJ == newCNPJ:
        print("\nValid CNPJ!\n")
    else:
        print("\nInvalid CNPJ!\n")
