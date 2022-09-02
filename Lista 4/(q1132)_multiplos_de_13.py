x = int(input()); y = int(input())
lista = [x,y] ; lista.sort()

menor = lista[0] ; maior = lista[1]

multiplos = 0
while menor <= maior:

    if menor %13 != 0:
        multiplos += menor
    menor += 1

print(multiplos)
