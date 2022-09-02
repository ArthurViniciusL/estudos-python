n = int(input())
voltas = 0
dentro = 0
fora = 0

while voltas < n:
    x = int(input())
    if x >= 10 and x <= 20:
        dentro += 1
    else:
        fora += 1
    voltas += 1

print("%i in" %dentro)
print("%i out" %fora)