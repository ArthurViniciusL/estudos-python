idadeDIAS = int(input())

anos = int(idadeDIAS / 365)
saldo = idadeDIAS - anos * 365
meses = int(saldo / 30)
dias = saldo - meses * 30

print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")