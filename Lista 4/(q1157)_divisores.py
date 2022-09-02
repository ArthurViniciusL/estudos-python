numero = int(input())

loop = 1                      #<- começa em 1 porque o divisor não pode ser 0
while loop <= numero:
    divisivel = numero % loop #<- essa var é necessario p/ não tratar a divisão como if. O result é o importante
    loop += 1
    if divisivel == 0:
        print(loop-1) 

#divisor: meu n° variavel % dos outros n° == 0