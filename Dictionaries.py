

customer = {"Id":70100100, "name": "Pepito"}

customer2 = {70100100: ["Pepito", "Perez" , 1234567.67], 70200200 : ["Maria", "Castro" , 2300000]} 

##Get()
print(customer2.get(70100100))

##Agregar elementos a la lista:

customer2[70300300] = ["Luis", "Garcia", 3000000.35]



customer2.update({70400400:["Ana", "Garcia", 3500000.35]})

print(customer2)


for i,j in customer2.items():
    print(i,j)