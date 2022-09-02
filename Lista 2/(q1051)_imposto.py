salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
    print("Isento")

elif salario > 2000.00 and salario <= 3000.00:
    debido = salario - 2000.00
    taxaIR = (debido * 8)/100
    print("R$ %.2f" %taxaIR)

elif salario > 3000.00 and salario <= 4500.00:
    debido = salario - 3000.00
    taxaIR = ((debido * 18)/100)+80
    print("R$ %.2f" % taxaIR)

elif salario > 4500.00:
    debido = salario - 4500.00
    taxaIR = ((debido * 28) /100) +80+270
    print("R$ %.2f" %taxaIR)
