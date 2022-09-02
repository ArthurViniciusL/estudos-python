x = int(input()); y = int(input())

if x < y:
    x += 1
    x = x
    while x < y:
        if x %5 == 2 or x %5 == 3:
            print(x)
        x += 1

else:
    y += 1
    y = y
    while y < x:
        if y %5 == 2 or y %5 == 3:
            print(y)
        y += 1
