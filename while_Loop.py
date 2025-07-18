

init = int(input("Ingrese 1 para comenzar , 0 para detener"))


categoria_A = 4500
categoria_B = 18900
categoria_C = 50000

while init == 1:

    cat_paciente = int(input("Indique la categoria del paciente:\n 1: A \n 2: B \n 3:C"))

    if cat_paciente == 1:
        print(f"Cobro paciente = {categoria_A}")
    elif cat_paciente ==2:
        print(f"Cobro paciente = {categoria_B}")
    elif cat_paciente == 3: 
        print(f"Cobro paciente = {categoria_C}")      
    else:
        print(f"Valide la categoria") 

    
    init = int(input("Desea validar otro paciente 1. Si 0. No"))
