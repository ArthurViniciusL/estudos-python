numero = int(input())

loop = 1
fim = 10000

while loop <= fim:
    if loop %numero == 2:
        print(loop)
    loop += 1
    