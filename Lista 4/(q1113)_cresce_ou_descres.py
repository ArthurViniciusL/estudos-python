A, B = str(input()).split(); n1 = int(A); n2 = int(B)

x = n1; y = n2
while n1 != n2:
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
    A, B = str(input()).split()
    n1 = int(A); n2 = int(B); x = n1; y = n2
    