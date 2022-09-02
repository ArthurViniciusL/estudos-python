numero_casos = int(input())

loop1 = 0
while (loop1 < numero_casos):
    numero = int(input())
    divisores = 0
    for c in range(1,numero+1):
	    if (numero % c) == 0:
		    divisores +=1

    if (divisores == 2):
        print("%i eh primo" %numero)
    else:
         print("%i não eh primo" %numero)
    loop1 += 1
    