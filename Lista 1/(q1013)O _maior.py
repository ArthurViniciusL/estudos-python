a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)
maiorAB = (a+b+abs(a-b))/2
#print("AB",int(maiorAB))

maiorC = (maiorAB+c+abs(maiorAB-c))/2
print(int(maiorC),"eh o maior")
