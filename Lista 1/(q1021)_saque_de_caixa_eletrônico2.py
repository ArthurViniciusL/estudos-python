saldo_total = float(input())

moneyNotas = [100, 50, 20, 10, 5, 2]
moneyMoedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for notas in moneyNotas:
    NumMoneyN = int(saldo_total / notas) #saber a quantidade de cédulas
    print("{} nota(s) de R$ {:.2f}".format(NumMoneyN, notas))
    saldo_total -= NumMoneyN * notas #stop do laço

print("MOEDAS:")
for moedas in moneyMoedas:
    NumMoneyM = int(round(saldo_total,2) / moedas)
    print("{} moeda(s) de R$ {:.2f}".format(NumMoneyM, moedas))
    saldo_total -= NumMoneyM * moedas