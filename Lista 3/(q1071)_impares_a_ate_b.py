num1 = int(input())
num2 = int(input())

if num1 > num2:
    laco = num2 +1
    soma = 0
    while laco < num1:
        if laco % 2 != 0:
            soma+=laco
        laco+=1
    print(soma)

elif num1 < num2:
    laco = num1 +1
    soma = 0
    while laco < num2:
        if laco % 2 != 0:
            soma+=laco
        laco+=1
    print(soma)

else:
    print(0)