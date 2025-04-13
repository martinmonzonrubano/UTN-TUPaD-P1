frase=input("Dime una frase o palabra: ")
ultletra=frase[len(frase)-1]
if ultletra=='a' or ultletra=='e' or ultletra=='i' or ultletra=='o' or ultletra=='u':
    print(f"{frase}!")
else:
    print(frase)