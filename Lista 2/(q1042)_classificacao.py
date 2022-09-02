#metodo 1:
A, B, C = input().split()
n1 = int(A)
n2 = int(B)
n3 = int(C)

if (n1 <= n2 and n1 <= n3) and (n2 <= n3):
    print("{}\n{}\n{}".format(n1,n2,n3))

elif (n2 <= n1 and n2 <= n3) and (n1 <= n3):
    print("{}\n{}\n{}".format(n2,n1,n3))

elif (n3 <= n1 and n3 <= n2) and (n2 <= n1):
    print("{}\n{}\n{}".format(n3,n2,n1))

elif (n1 <= n2 and n1 <= n3) and (n3 <= n2):
    print("{}\n{}\n{}".format(n1,n3,n2))

elif (n2 <= n1 and n2 <= n3) and (n3 <= n1):
    print("{}\n{}\n{}".format(n2,n3,n1))

elif (n3 <= n1 and n3 <= n2) and (n1 <= n2):
    print("{}\n{}\n{}".format(n3,n1,n2))

print("")
print("{}\n{}\n{}".format(n1,n2,n3))

#metodo 2:
'''A, B, C = input().split()

n1 = int(A)
n2 = int(B)
n3 = int(C)
lista = [n1, n2, n3]

lista.sort()
print("{}\n{}\n{}".format(lista[0],lista[1],lista[2]))
print("")
print("{}\n{}\n{}".format(n1,n2,n3))
'''