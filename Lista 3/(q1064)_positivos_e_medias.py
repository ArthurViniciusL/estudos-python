voltas = 0
positivos = 0
nume = 0
while voltas < 6:
    num = float(input())
    if num > 0:
        positivos += 1
        nume += num
    voltas += 1

media = nume / positivos
print("%i valores positivos\n%.1f" %(positivos,media))
