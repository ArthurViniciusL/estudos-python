casos = int(input())

d = 1
while d <= casos: #for c in range(casos):
    A, B = str(input()).split()
    x = int(A) ; y = int(B)

    if y > 0 or y <0:
        divisao = x/y
        print(divisao)
    
    else:
        print("divisao impossivel")
    
    d += 1
    