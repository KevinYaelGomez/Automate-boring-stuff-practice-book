#Conway's Game Life
#Es una simulacion donde celulas se mueven, se duplican y mueren. Si una celula tiene 2 o más celulas vivas a su alrededor, entonces en la siguiente fase se mantiene con vida, de lo contrario pasa a ser una celula muerta.

import random, time, copy
WIDTH = 60
HEIGHT = 20

nextcell = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#") #Celula viva
        else:
            column.append(" ") #Celula muerta
    nextcell.append(column)

while True:
    print('\n\n\n\n\n')
    currentCell = copy.deepcopy(nextcell)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCell[x][y], end='')
        print()

    #Calcula la siguiente fase tomando la posiciones de las celulas
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Cordenadas de las celulas vecinas
            #%Width y %Height evita que se salga del grafo
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            numNeighbors = 0
            if currentCell[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 
            if currentCell[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCell[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCell[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCell[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCell[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCell[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCell[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            #Definir las reglas 
            if currentCell[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextcell[x][y] = '#'
            elif currentCell[x][y] == ' ' and numNeighbors == 3:
                nextcell[x][y] = '#'
            else:
                nextcell[x][y] = ' '
    time.sleep(5)