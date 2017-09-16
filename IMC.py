# encoding UTF-8
# Autor: Andrea Montero Rivas, A01374496
# Descripcion: Convierte numero decimal a romano.

def calcularIMC(peso, altura):
    IMC=peso/(altura**2)
    return IMC

def indiceDeEstadoIMC(IMC):
    if IMC<=0:
        print ("ERROR")
    elif IMC<18.5:
        estadoIMC="Bajo peso"
        return estadoIMC
    elif IMC>=18.5 and IMC<=25:
        estadoIMC = "Peso normal"
        return estadoIMC
    elif IMC>25:
        estadoIMC = "Sobrepeso"
        return estadoIMC

def main():
    peso=int(input("Escribe el peso en kilogramos",))
    estatura=int(input("Escribe la estatura en metros",))
    IMC = calcularIMC(peso, estatura)
    estadoIMC = indiceDeEstadoIMC(IMC)
    print("Estado de IMC:", estadoIMC)

main()
