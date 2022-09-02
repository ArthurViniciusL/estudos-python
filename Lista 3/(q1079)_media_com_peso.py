tamanho = int(input())

loop = 0

while loop < tamanho:
    A, B, C = input().split()
    n1 = float(A); n2 = float(B); n3 = float(C)
    p1 = 2; p2 = 3; p3 = 5 #pesos
    media = ((n1*p1)+(n2*p2)+(n3*p3)) / (p1+p2+p3)
    print("%.1f" %media)
    loop += 1
    