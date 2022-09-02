A, B = input().split()
x = int(A); y = int(B)

quadr1 = x; quadr2 = y #quadrantes 1 e 2

while quadr1 or quadr2 != 0:

    if quadr1 > 0 and quadr2 > 0: print("primeiro")
    elif quadr1 < 0 and quadr2 > 0: print("segundo")
    elif quadr1 < 0 and quadr2 < 0: print("terceiro")
    elif quadr1 > 0 and quadr2 < 0: print("quarto")
    else: break
    A, B = input().split()
    x = int(A); y = int(B)
    quadr1 = x; quadr2 = y