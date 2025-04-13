edad=int(input("Indique su edad: "))
if edad<12: 
    print("Usted pertenece a la categoria niño")
elif 12<edad<18:
    print("Usted pertenece a la categoria adolecente")
elif 18>=edad<30:
    print("Usted pertenece a la categoria Adulto/a joven")
else:
    print("Usted pertenece a la categoria Adulto")