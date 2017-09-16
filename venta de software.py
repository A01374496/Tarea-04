# encoding UTF-8
# Autor: Andrea Montero Rivas, A01374496
# Descripcion: Convierte numero decimal a romano.

def calcularDescuento(precio, cantidad):
    if cantidad >= 10 and cantidad<= 19:
        precioConDescuento = precio - precio * 0.20
        return precioConDescuento
    if cantidad >= 20 and cantidad<= 49:
        precioConDescuento = precio - precio * 0.30
        return precioConDescuento
    if cantidad >= 50  and cantidad<= 99:
        precioConDescuento = precio - precio * 0.40
        return precioConDescuento
    if cantidad >= 100:
        precioConDescuento = precio - precio * 0.50
        return precioConDescuento
    else:
        print ("ERROR")

def main():
    cantidad = int(input("Paquetes comprados:",))
    precio = 1500 * cantidad
    precioConDescuento = calcularDescuento(precio, cantidad)
    print ("El total a pagar: $", precioConDescuento)

main()