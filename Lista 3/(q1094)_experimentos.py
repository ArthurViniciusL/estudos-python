n = int(input()) #total de casos para registro

loop = 0
coelho = 0
rato = 0
sapo = 0

while loop < n:
    A,B = input().split() #o total e tipo de animal
    
    valor = int(A)
    animal = str(B).lower()
    if animal == "c":
        coelho += valor
    
    elif animal == "r":
        rato += valor
    
    else:
        sapo += valor #animal == "s"
    loop += 1

total = coelho + rato + sapo #total de cobaias
print("Total: %i cobaias" %total)
print("Total de coelhos: %i" %coelho)
print("Total de ratos: %i" %rato)
print("Total de sapos: %i" %sapo)

#lA = [coelho,rato,sapo]
print("Percentual de coelhos: %.2f" %((coelho*100)/total),"%") #Percentual = (menor*100)/maior
print("Percentual de ratos: %.2f" %((rato*100)/total),"%")
print("Percentual de sapos: %.2f" %((sapo*100)/total),"%")
