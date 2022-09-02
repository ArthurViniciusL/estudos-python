A, B = input().split()

horas1 = int(A)
horas2 = int(B)

if horas1 < horas2:
    contador = 0
    for laco in range(horas1,horas2):
        contador +=1
    print("O JOGO DUROU %i HORA(S)" %contador)

elif horas1 > horas2:
    hora = 24 - (horas1 - horas2)
    print("O JOGO DUROU %i HORA(S)" %hora)

else:
    print("O JOGO DUROU 24 HORA(S)")
