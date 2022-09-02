A, B, C = input().split()

a = float(A)
b = float(B)
c = float(C)

dΔ = (b **2) - (4 * a * c) #calcule o delta

if a == 0:
    print("Impossivel calcular")

elif dΔ < 0:
    print("Impossivel calcular")

else:
    raiz1 = (-b + dΔ **(0.5)) / (2 * a) #escreva a formula
    print("R1 = {:.5f}".format(raiz1))

    raiz2 = (-b - dΔ **(0.5)) / (2 * a)
    print("R2 = %.5f" %raiz2)