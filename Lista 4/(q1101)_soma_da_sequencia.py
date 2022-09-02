A, B = str(input()).split()
lista = [A,B] ; lista.sort()

m = int(lista[0]); n = int(lista[1])

while not (m == 0) or (n == 0):
    soma = 0
    while (m <= n):
        print(m,end=" ")
        soma += m
        m +=1
    print("Sum=%i" %soma)

    A, B = str(input()).split()
    lista = [A,B] ; lista.sort()
    m = int(lista[0]); n = int(lista[1])

    
'''
A, B = str(input()).split()
lista = sorted([A,B])
m = int(lista[0]); n = int(lista[1])

while (m > 0) or (n > 0):
    soma = 0
    while (m <= n):
        print(m,end=" ")
        soma += m
        m +=1
    print("Sum=%i" %soma)

    A, B = str(input()).split()
    lista = sorted([A,B])
    m = int(lista[0]); n = int(lista[1])
    m = m; n = n
'''

'''
A, B = str(input()).split()
lista = sorted([A,B])
m = int(lista[0]); n = int(lista[1])

while (m != 0) and (n != 0):
    soma = 0
    while (m <= n):
        print(m,end=" ")
        soma += m
        m +=1
    print("Sum=%i" %soma)

    A, B = str(input()).split()
    lista = sorted([A,B])
    m = int(lista[0]); n = int(lista[1]);
    m = m; n = n
'''

''' Funciona:
aux = 0
maior = 0
menor = 0

cond = True
while cond:
        valor1, valor2 = map(int, input().split())
   
        if(valor1 <= 0 or valor2 <= 0):
                break

        maior = valor1 if valor1 > valor2 else valor2
        menor = valor2 if valor2 < valor1 else valor1
   
        if maior > menor :
                aux = maior
                maior = menor
                menor = aux
               
        soma = 0
       
        while maior <= menor :
         print(maior, end=' ')
         soma += maior
         maior+=1
        print("Sum=%d"%soma) 
'''