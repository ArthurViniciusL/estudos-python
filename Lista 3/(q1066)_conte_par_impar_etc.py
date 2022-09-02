laco = 0
pares = 0
impares = 0
positivos = 0
negativos = 0

while laco < 5:
    valores = int(input())

    if valores %2 == 0:
        pares += 1
    if valores %2 != 0:
        impares += 1
    if valores > 0:
        positivos += 1
    if valores < 0:
        negativos += 1
    laco += 1

print("%i valor(es) par(es)" %pares)
print("%i valor(es) impar(es)" %impares)
print("%i valor(es) positivo(s)" %positivos)
print("%i valor(es) negativo(s)" %negativos)
