tempoS = int(input())

segundos = [3600, 60, 1]
resultado = []
for laço in segundos:
    qtd = int(tempoS / laço)
    resultado.append(str(qtd))
    tempoS -= qtd * laço
print(":".join(resultado))

