testes = int(input())

for c in range(1,testes +1): # while loop < testes:
    A, B = str(input()).split()

    x = int(A) ; y = int(B)
    impares = 0

    if x > y: x = int(B) ; y = int(A)

    elif x < y: x = int(A) ; y = int(B)

    else: #x == y:
        impares = 0

    x = x+1
    while x < y:
        impar = x %2
        if impar == 1:
            impares += x
        x += 1
    print(impares)
