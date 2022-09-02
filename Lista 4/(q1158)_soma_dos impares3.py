tot_casos = int(input())           #<- total de casos a ser lido

loop1 = 0
while loop1 < tot_casos:

    A, B = str(input()).split()
    x = int(A) ; y = int(B)        #<- x é numero a ser lindo // y é o tamanho da sequência

    loop2 = 1
    sum_impares = 0                #<- acumulador dos impares
    while (loop2 <= y):            #<- em for ficaria: for loop2 in range (y+1)

        if x %2 == 1:
            sum_impares += x
            loop2 += 1
        x += 1                    #<- x = x + x pq eu preciso que o valor de x cresca sem ter alguém digitando o proximo valor de x

    print(sum_impares)

    loop1 += 1
    
