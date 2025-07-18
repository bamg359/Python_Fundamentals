
headers = ["Identificacion", "Nombre", "Apellido", "Salario","Telefono" "Activo","Correo"]


customer = []

id = int(input("Ingrese su id"))
customer.append(id)
name = input("Ingrese el nombre del empleado")
customer.append(name)
last_name = input("Ingrese el apellido")
customer.append(last_name)
salary = float(input("Ingrese el salario:"))
customer.append(salary)
phone= input("INgrese número de  telefono: ")
customer.append(phone)
isActive = bool(input("Coloque Estado 1. Activo 0. Inactivo "))
customer.append(isActive)
email = input("Ingrese correo: ")
customer.append(email)


for i in range(len(headers)):
    for j in range(len(customer)):
        if i==j:
            print(f"{headers[i]}:{customer[j]}")
            continue
