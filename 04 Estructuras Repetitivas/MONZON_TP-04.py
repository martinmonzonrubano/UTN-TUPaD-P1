#1)Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
num=abs(int(input("Escriba un numero: "))) #Abs por si es negativo para que el while sea posible
contador=1 #Inicializando en uno me ahorro el if especial para el 0
while num>=10: #Todos los numeros de una cifra ya estan previsto por eso el 10
    contador+=1
    num//=10
print(f"El numero tiene {contador} digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
sumatoria=0
if num1<num2:
    menor=num1
    mayor=num2
else:
    menor=num2
    mayor=num1
for i in range (menor+1, mayor):
    sumatoria+=i
print(f"La suma de los valores enteros entre {menor} y {mayor} es: {sumatoria}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
sumatoria=0
num=int(input("Ingrese un numero: "))
while num!=0:
    sumatoria+=num
    num=int(input("Ingrese un numero: "))
print(f"La suma de estos numeros es de {sumatoria}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número
import random
num_aleatorio=random.randint(0,9)
num=int(input("Intente adivinar un numero aleatorio del 0 al 9: "))
while num!=num_aleatorio:
    print("Numero Equivocado")
    num=int(input("Intente adivinar un numero aleatorio del 0 al 9: "))
print("Usted adivino el numero!")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range (100, -1, -1):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
sumatoria=0
num_pos=int(input("Indique un numero entero positivo: "))
while num_pos<0:
    print("Ese no es un numero positivo")
    num_pos=int(input("Indique un numero entero positivo: "))
for i in range (0, num_pos+1):
    sumatoria+=i
print(f"El total de la suma de los numeros entre 0 y {num_pos} es de: {sumatoria}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
num_par=0
num_impar=0
num_neg=0
num_pos=0
for i in range (1, 11):
    num=int(input(f"Indique el numero {i}: "))
    if num>=0:
        num_pos+=1
    else:
        num_neg+=1
    if num%2==0:
        num_par+=1
    else:
        num_impar+=1
print(f"El numero de numeros pares es de: {num_par}")
print(f"El numero de numeros impares es de: {num_impar}")
print(f"El numero de numeros positivos es de: {num_pos}")
print(f"El numero de numeros negativos es de: {num_neg}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
div=0
sumatoria=0
for i in range (1,101):
    num=int(input(f"Escriba el numero nro{i}: "))
    div+=1
    sumatoria+=num
promedio=sumatoria/div
print(f"La media de los numeros indicados es de: {promedio}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num=int(input("Ingrese un numero: "))
num_invertido=0
while num>0:
    ultimo_dig=num%10 
    num_invertido=num_invertido*10+ultimo_dig
    num=num//10
print(num_invertido)
