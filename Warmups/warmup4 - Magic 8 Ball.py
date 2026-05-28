import random

magic8ball = [
    "Si",
    "No", 
    "Tal vez",
    "Depende de como lo veas",
    "2 de pastor con todo",
    "Es muy probable",
    "El que no arriesga, no gana",
    "No te entiendo"
]

while True:
    respuesta = input("Preguntame lo que quieras: ")
    if respuesta != "":
        print(random.choice(magic8ball))
        print()
    else:
        break