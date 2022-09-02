notas = 0; soma = 0
valido = 0

while valido < 2:
    nota = float(input())
    notas = nota
    if notas < 0.0 or notas > 10.0: #Fora do parametro [0...10]
        print("nota invalida")
    else:                           #Dentro do parametro [0...10]
        soma += notas
        valido += 1

media = soma/valido; print("media = %.2f" %media)
