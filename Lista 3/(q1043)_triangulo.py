A, B, C = input().split()

a = float(A)
b = float(B)
c = float(C)

if (a + b) > c and (b + c) > a and (a + c) > b:
    Peri = (a + b + c)
    print("Perimetro = {:.1f}".format(Peri))

else:
    areaTrap = ((a + b) * c)/2
    print("Area = {:.1f}".format(areaTrap))