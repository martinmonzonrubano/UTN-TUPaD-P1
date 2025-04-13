import random
from statistics import mode, mean, median
numeros_aleatorios = [random.randint(1, 100) for i in range(100)]
moda=mode(numeros_aleatorios)
media=mean(numeros_aleatorios)
mediana=median(numeros_aleatorios)
if media==moda and media==mediana:
    print("Sin sesgo")
else:
    if media<mediana and mediana<moda:
        print("Sesgo negativo o a la izquierda")
    else:
        if media>mediana and mediana>moda:
            print("Sesgo positivo o a la derecha")