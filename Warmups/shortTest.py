def for_loop():
    for i in range(1,11):
        print(i)

def while_loop():
    x = 0
    while True:
        x += 1
        print(x)
        
        if x == 10:
            break

for_loop()
print()
while_loop()