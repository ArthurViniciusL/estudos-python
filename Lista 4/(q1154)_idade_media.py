idade = int(input())

somaIdades = idade #Começa recebendo a var idade, depois começa receber as idades dentro do laço
voltas = 0
while idade >= 0:
    idade = int(input())
    if idade >= 0:
        somaIdades += idade
    voltas += 1
    #o laços para quando recebe um número negativo
media = somaIdades/voltas; print("%.2f" %media)
