numero = int(input())

if numero %2 != 0:
    print(numero)
    
voltas = 0
while voltas <= 10:
    numero += 1
    if (numero % 2) != 0:
        print(numero)
    voltas += 1
