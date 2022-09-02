A, B, C = input().split()

ladoA = float(A) #;print(ladoA)
ladoB = float(B) #;print(ladoB)
ladoC = float(C) #;print(ladoC)

if ladoA < ladoB:
    menor = ladoA; ladoA = ladoB; ladoB = menor
if ladoA < ladoC:
    menor = ladoA; ladoA = ladoC; ladoC = menor
if ladoB < ladoC:
    menor = ladoB; ladoB = ladoC; ladoC = menor

if ladoA >= (ladoB + ladoC): print("NAO FORMA TRIANGULO")
else:
    if (ladoA**2) == (ladoB**2) + (ladoC**2): print("TRIANGULO RETANGULO")
    if (ladoA**2) > (ladoB**2) + (ladoC**2): print("TRIANGULO OBTUSANGULO")
    if (ladoA**2) < (ladoB**2) + (ladoC**2): print("TRIANGULO ACUTANGULO")
    if ladoA == ladoB and ladoB == ladoC and ladoA == ladoC: print("TRIANGULO EQUILATERO")
    else:
        if (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC): print("TRIANGULO ISOSCELES")
