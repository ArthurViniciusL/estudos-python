numero = int(input())

antecessores = 1 ; fatorial = 1

while antecessores <= numero:
    fatorial *= antecessores ; antecessores += 1
print(fatorial)