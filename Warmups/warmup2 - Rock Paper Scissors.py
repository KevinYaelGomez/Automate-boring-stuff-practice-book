import random, sys

wins = 0
losses = 0
ties = 0
print("Piedra, Papel o Tijera")
print("Escoge 1 para piedra, 2 para papel y 3 para tijera. Presiona 0 para salir.\nEmpezemos.\n")

while True:
    #Lo del %s esta genial :o
    print('%s Ganadas, %s Perdidas, %s Empates' % (wins, losses, ties))
    while True:
        respuesta = int(input())

        if respuesta == 0:
            sys.exit()
        elif respuesta == 1 or respuesta == 2 or respuesta == 3:
            break

        print("Valor no valido.\n")

    randomNum = random.randint(1,3)

    if randomNum == 1:
        rivalChose = 1
        print("El rival eligio piedra.")
    elif randomNum == 2:
        rivalChose = 2
        print("El rival eligio papel.")
    elif randomNum == 3:
        rivalChose = 3
        print("El rival eligio tijeras.")

    if respuesta == rivalChose:
        ties += 1
        print("Fue un empate.\n")
    elif respuesta == 1 and rivalChose == 3:
        wins += 1
        print("Ganaste :D.\n")
    elif respuesta == 1 and rivalChose == 2:
        losses += 1
        print("Perdiste :(\n")
    elif respuesta == 2 and rivalChose == 1:
        wins += 1
        print("Ganaste :D.\n")
    elif respuesta == 2 and rivalChose == 3:
        losses += 1
        print("Perdiste :(\n")
    elif respuesta == 3 and rivalChose == 2:
        wins += 1
        print("Ganaste :D.\n")
    elif respuesta == 3 and rivalChose == 1:
        losses += 1
        print("Perdiste :(\n")
