

costo = float(input("Ingrese el costo del producto"))

margen_ganancia = float(input("Ingrese el margen deseado"))


def calcular_precio_prod(costo, margen_ganancia):

    precio = costo/(1 - (margen_ganancia/100))

    return round(precio, 2)



precio_prod = calcular_precio_prod(costo, margen_ganancia)

print(f"Precio producto: ${precio_prod}")



