saldo_total = int(input())
moneyNotas = [100, 50, 20, 10 , 5, 2, 1] #valor das cédulas

print(saldo_total)#exibir o saldo

for notas in moneyNotas:
    NumMoneyN = int(saldo_total / notas) #saber a quantidade de cédulas
    print("{} nota(s) de R$ {},00".format(NumMoneyN, notas))
    saldo_total -= NumMoneyN * notas #stop do laço