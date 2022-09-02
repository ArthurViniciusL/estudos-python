n = int(input())

loop = 0
pares = 0

while loop < n:
    if loop %2 == 0:
        pares += 2
        quadrado = pares ** 2
        print("%i^2 = %i" %(pares,quadrado))
    loop += 1
