A, B = input().split()

n1 = int(A)
n2 = int(B)

'''divisao = n2 // n1 ; print("D:",divisao)
multiplos = divisao * n1 ; print("M:",multiplos)'''

multiplos = n1 % n2 and n2 % n1 ; #print("M:", multiplos)

if multiplos == 0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")