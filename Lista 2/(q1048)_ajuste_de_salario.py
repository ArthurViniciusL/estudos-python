salAtual = float(input())

if salAtual > 0 and salAtual <= 400:
    ajuste = (salAtual * (15/100))
    salNovo = salAtual + ajuste
    print("Novo salario: %.2f" %salNovo);print("Reajuste ganho: %.2f" %ajuste)
    print("Em percentual: 15 %")

elif salAtual >= 400.01 and salAtual <= 800:
    ajuste = (salAtual * (12/100))
    salNovo = salAtual + ajuste
    print("Novo salario: %.2f" %salNovo);print("Reajuste ganho: %.2f" %ajuste)
    print("Em percentual: 12 %")

elif salAtual >= 800.01 and salAtual <= 1200:
    ajuste = (salAtual * (10/100))
    salNovo = salAtual + ajuste
    print("Novo salario: %.2f" %salNovo);print("Reajuste ganho: %.2f" %ajuste)
    print("Em percentual: 10 %")

elif salAtual >= 1200.01 and salAtual <= 2000:
    ajuste = (salAtual * (7/100))
    salNovo = salAtual + ajuste
    print("Novo salario: %.2f" %salNovo);print("Reajuste ganho: %.2f" %ajuste)
    print("Em percentual: 7 %")

else:
    ajuste = (salAtual * (4/100))
    salNovo = salAtual + ajuste
    print("Novo salario: %.2f" %salNovo);print("Reajuste ganho: %.2f" %ajuste)
    print("Em percentual: 4 %")