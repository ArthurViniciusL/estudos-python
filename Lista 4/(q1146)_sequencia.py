numero = int(input())

while (numero != 0):
    loop = 0
    while loop < numero:
        loop += 1
        print(loop, end= " ")
    print()
    numero = int(input())
    
'''while True:
    numero= int(input())
    if(numero == 0):
        break
        
    space = ""
    for i in range(1,numero+1):
        space += str(i) + " "
    print(space[:-1])'''