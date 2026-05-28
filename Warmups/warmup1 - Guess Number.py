import random

secretNum = random.randint(1, 20)
print("Adivina en que numero estoy pensando del 1 al 20.\nTienes 6 intentos")

for x in range(1,7):
    respuesta = int(input())
    print()

    if respuesta < secretNum:
        print("El numero es más grande.")
    elif respuesta > secretNum:
        print("El numero es más pequeño")
    else:
        break

if respuesta == secretNum:
    print("Felicidades, " + str(secretNum) + " era el numero correcto :D")
else:
    print("Incorrecto, el numero era " + str(secretNum) + " :(")