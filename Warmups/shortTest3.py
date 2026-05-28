supplies = ["Lapiz", "Engrapadora", "Lanzallamas", "Esposas"]

for i in range(len(supplies)):
    print("El index " + str(i) + " en supplies es: " + supplies[i])
    
print()

#La funcion enumerate() en un "for loop" regresa 2 valores: Index del item y el item en si
for index, item in enumerate(supplies):
    print("El index " + str(index) + " en supplies es: " + item)