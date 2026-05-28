user = int(input("Ingresa un numero: "))

def collatz(number):
    if number % 2 == 0:
        r = number // 2
    elif number % 2 == 1:
        r = 3 * number + 1
    return r

res = collatz(user)
print(res)

try:
    while res != 1:
        res = collatz(res)
        print(res)

except ValueError:
    print("Tiene que ser un valor integro.")
    pass