#cnpj: 04.252.011/0001-10, 40.688.134/0001-61, 71.506.168./0001-11, 12.544.992/0001-05
import CNPJ

cnpj = "04.252.011/0001-10"
    
cleanCNPJ = CNPJ.cnpjCleanFormat(cnpj)

try:
    if CNPJ.validate(cleanCNPJ):
        noDigitCNPJ = cleanCNPJ[:12]

        firstDigit = CNPJ.calcFirstDig(noDigitCNPJ)

        oldCNPJ = noDigitCNPJ + str(firstDigit)

        secondDigit = CNPJ.calcSecondDig(oldCNPJ)

        newCNPJ = oldCNPJ + str(secondDigit)

        CNPJ.verifyCNPJ(cleanCNPJ, newCNPJ)
    else:
        print("\nSequence not allowed!\n")
except IndexError:
    print("\nLetters not allowed!\n")
    