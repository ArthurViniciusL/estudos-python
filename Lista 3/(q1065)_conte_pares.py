voltas = 0
pares = 0
while voltas <= 4:
    numero = int(input())
    if numero %2 == 0:
        pares += 1
    voltas += 1
print("%i valores pares" %pares)