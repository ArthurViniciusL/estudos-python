A, B = input().split()

x = float(A)
y = float(B)

if x == 0.0 and y == 0.0:
        print("Origem")

elif x > 0.0 and y > 0.0:
    print("Q1")

elif x < 0.0 and y > 0.0:
    print("Q2")

elif x < 0.0 and y < 0.0:
    print("Q3")

elif x > 0.0 and y < 0.0:
    print("Q4")

elif x > 0.0 or x < 0.0 and y == 0.0:
    print("Eixo X")

elif x == 0.0 and y > 0.0 or y < 0.0:
    print("Eixo Y")
