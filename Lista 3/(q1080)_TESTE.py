'''
Código do github:

maior = 0
lista = {}
posicao = 0
while posicao < 100:
    valor = int(input())
    if(valor > maior):
        maior = valor
        lista[valor] = posicao
    posicao += 1
print(maior)
print(lista[maior]+1)
----------------------------------
Código simplificado:

newMaior = 0
posicao = 0
fim = 100
loop = 0
while loop < fim:
    n = int(input())
    if(n > newMaior):
        newMaior = n
        print("Maior:",newMaior)
        posicao = loop
        print("Posição:",posicao)
    loop += 1
print(newMaior)
print(posicao+1)
----------------------------------
Meu código robô:

newMaior = 0
posicao = 0
fim = 100
loop = 0
while loop < fim:
    from random import randint
    n = randint(1,100)
    #n = int(input())
    print(n)
    if n > newMaior:
        newMaior = n
        #print("Maior:",newMaior)
        posicao = loop
        #print("Posição:",posicao)
    loop += 1
print(">>>", newMaior)
print(">>>", posicao+1)
----------------------------------
Meu código final:

newMaior = 0
posicao = 0
fim = 100
loop = 0
while loop < fim:
    #from random import randint
    #n = randint(1,100)
    n = int(input())
    #print(n)
    if n > newMaior:
        newMaior = n
        #print("Maior:",newMaior)
        posicao = loop
        #print("Posição:",posicao)
    loop += 1
print(">>>", newMaior)
print(">>>", posicao+1)
----------------------------------
Pergunta: Por que print(">>>", posicao+1) muda tanto sem o +1???
'''