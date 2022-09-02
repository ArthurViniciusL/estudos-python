numero = int(input())
laço = numero
while (laço != 0):
  
    soma = 0
    #loop = 0
    for loop in range (10): #while loop < 5:
        if numero %2 == 0:
            soma += numero
            #print(">>>",loop)
            #loop += 1
        numero += 1
    print(soma)

    numero = int(input()) ; laço = numero
