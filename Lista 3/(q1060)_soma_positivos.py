voltas = 0
positivos = 0
while voltas < 6:
    n = float(input())
    if n > 0:
        positivos += 1
    voltas +=1
print("%i valores positivos" %positivos)