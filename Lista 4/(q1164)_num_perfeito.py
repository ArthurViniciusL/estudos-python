tamanho_loop = int(input())

loop = 0
while loop < tamanho_loop: #for loop in range(tamanho_loop):

    numero = str(input())
    numero_final = int(numero[-1]) #<- converto a var de str p/ int e solicito apenas o seu final.

    if numero_final == 6 or numero_final == 8: #<- todo n° 'perfeito' termina em 6 ou 8.
        print("%s eh perfeito" %numero)
    
    else:
        print("%s nao eh perfeito"%numero)
    
    loop += 1

#Teste: #n = input() ; tamanho = list(n) ; num = int(n[-1]) ; print(num)