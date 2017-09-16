# encoding UTF-8
# Autor: Andrea Montero Rivas, A01374496
# Descripcion: Mezcla de dos colores.

def mezclarColores(color1, color2):
    if (color1==color2):
        colorResultante = color1
        return colorResultante

    elif ((color1 == "rojo") or (color2 == "rojo")) and ((color2 == "azul") or (color1 == "azul")):
        colorResultante= "morado"
        return colorResultante

    elif ((color1 == "rojo") or (color2 == "rojo")) and ((color2 == "amarillo") or (color1 == "amarillo")):
        colorResultante = "naranja"
        return colorResultante

    elif ((color1 == "azul") or (color2 == "azul")) and ((color2 == "amarillo") or (color1 == "amarillo")):
        colorResultante = "verde"
        return colorResultante
    else:
        colorResultante = "ERROR"
        return colorResultante


def main():
    color1 = raw_input("Teclea un color primario (rojo, azul o amarillo)", )
    color1Minuscula = color1.lower()
    color2 = raw_input("Teclea otro color primario (rojo, azul o amarillo)", )
    color2Minuscula = color2.lower()
    colorResultante = mezclarColores(color1Minuscula, color2Minuscula)
    print (colorResultante)

main()
