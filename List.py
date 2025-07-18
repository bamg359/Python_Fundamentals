
## Listas son mutables 
## Aceptan diferentes tipos de datos 
## Tienen metodos que permiten manipular
## Son Iterables


customer = [70100100, "Pepito", "Perez", 1590000.24, True]


print(type(customer))


#Para acceder a un elemento dentro de la lista 
print(customer[4])

## Si quiero agregar un nuevo elemento 

customer.append( "pp@mail.com")

print(customer[5])

##Agregar en una posicion especifica

customer.insert(4,"3214567890" )
print(customer[4])
##print(customer)


##como Saber el tamaño de la lista

print(len(customer))

# Como recorrer una lista usando un while 

contar = 0

while contar < len(customer):
    print(customer[contar])
    contar+=1
