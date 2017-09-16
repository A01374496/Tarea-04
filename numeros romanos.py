# encoding UTF-8
# Autor: Andrea Montero Rivas, A01374496
# Descripcion: Convierte numero decimal a romano.

def convertirARomano(decimal):
    if decimal>1 and  decimal<4:
        numRomano=decimal * "I"
        return numRomano

    elif decimal ==4 :
        numRomano ="IV"
        return numRomano

    elif decimal>4 and decimal<9 :
        numRomano ="V"+ (decimal%5*"I")
        return numRomano

    elif decimal==9 or decimal==10:
        numRomano =(decimal%2*"I")+"X"
        return numRomano

    else:
        numRomano ="Error. Valor fuera del rango."
        return numRomano


def main():
    numDecimal = int(input("Teclea un numero del 1 al 10 ", ))
    numRomano = convertirARomano(numDecimal)
    print (numRomano)


main()
