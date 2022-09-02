A, B = input().split()

lanche = int(A)
quantia = int(B)

if lanche == 1:
    print("Total: R$ {:.2f}".format(4.00 * quantia))

elif lanche == 2:
    print("Total: R$ {:.2f}".format(4.50 * quantia))

elif lanche == 3:
    print("Total: R$ {:.2f}".format(5.00 * quantia))

elif lanche == 4:
    print("Total: R$ {:.2f}".format(2.00 * quantia))

else:
    print("Total: R$ {:.2f}".format(1.50 * quantia))
