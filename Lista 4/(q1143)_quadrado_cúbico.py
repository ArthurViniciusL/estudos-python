linhas = int(input())

loop = 1
while loop <= linhas:
    quadrado = loop **2; cubo = loop **3
    print("%i %i %i" %(loop, quadrado, cubo))
    loop += 1

'''for loop in range(1,linhas+1):
    quadrado = loop **2; cubo = loop **3
    print("%i %i %i" %(loop, quadrado, cubo))'''