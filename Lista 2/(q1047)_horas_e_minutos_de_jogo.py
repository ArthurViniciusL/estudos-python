A, B, C, D = input().split()

horaIni = int(A)
minutIni = int(B)

horaFim = int(C)
minutFim = int(D)

if horaIni < horaFim:
    newHora = horaFim - horaIni
    if minutIni < minutFim:
        newMinut = minutFim - minutIni
    elif minutIni > minutFim:
        newHora = newHora - 1
        newMinut = (60 - minutIni) + minutFim
    else:
        #minutIni == minutFim:
        newMinut = 0

elif horaIni > horaFim:
    newHora = (24 - horaIni) + horaFim
    if minutIni < minutFim:
        newMinut = minutFim - minutIni
    elif minutIni > minutFim:
        newHora = newHora - 1
        newMinut = (60 - minutIni) + minutFim
    else:
        newMinut = 0

elif horaIni == horaFim:
    if minutIni < minutFim:
        newMinut = minutFim - minutIni
        newHora = 0
    elif minutIni > minutFim:
        newMinut = (60 - minutIni) + minutFim
        newHora = 23
    else:
        newHora = 24
        newMinut = 0
    
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(newHora, newMinut))
