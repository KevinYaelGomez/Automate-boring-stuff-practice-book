catNames = []

while True:
    print("Ingresa el nombre del gato " + str(len(catNames) + 1) + " (O ingresa nada para terminar): ")
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #Lista concatenada

print("El nombre de los gatos son: ")
for name in catNames:
    print(" " + name)