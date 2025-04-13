nombre=input("Cual es su nombre? ")
opc=int(input("Indique que opcion desea 1, 2 o 3: "))
if opc==1:
    print(nombre.upper()) 
else:
    if opc==2:
        print(nombre.lower())
    else:
        if opc==3:
            print(nombre.title())
        else:
            print("Opcion Invalida!")