A, B, C, D = input().split()

n1 = float(A)
n2 = float(B)
n3 = float(C)
n4 = float(D)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) /10 #-> pesos (2 + 3 + 4 + 1)
print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame: %.1f" %n5)
    newMedia = (media + n5) /2

    if newMedia >= 5.0:
         print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" %newMedia)