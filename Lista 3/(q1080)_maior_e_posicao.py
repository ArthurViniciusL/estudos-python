newMaior = 0
posicao = 0
fim = 100
loop = 0

while loop < fim:
    n = int(input())
    if n > newMaior:
        newMaior = n
        posicao = loop
    loop += 1
print(newMaior)
print(posicao+1)
