contra=input("Ingrese su nueva contraseña:")
cantidad=int(len(contra))
if cantidad<14 and cantidad>8:
    print("Ha ingresado una clave correcta")
else:
    print("Ha ingresado una clave incorrecta, porfavor ingrese una de entre 8 y 14 caracteres")