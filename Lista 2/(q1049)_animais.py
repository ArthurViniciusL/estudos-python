parametro1 = str(input()).strip().lower()#Tipo /.strip() remove espaço da direita e esquerda
parametro2 = str(input()).strip().lower()#Classe
parametro3 = str(input()).strip().lower()#Ordem
#print(Espécie)

listTipo = ["vertebrado","invertebrado"]
listClasse = ["ave","mamifero","inseto","anelideo"]
listOrdem = ["carnivoro","onivoro","herbivoro","hematofago"]
listEspecie = ["aguia","pomba","homem","vaca","pulga","lagarta","sanguessuga","minhoca"]
 
#vertebrados: L12 - L23
if parametro1 == listTipo[0]:
    if parametro2 == listClasse[0]:
        if parametro3 == listOrdem[0]:
            print(listEspecie[0]) #aguia
        
        else:
            print(listEspecie[1]) #pomba

    elif parametro2 == listClasse[1]:
        if parametro3 == listOrdem[1]:
            print(listEspecie[2]) #homem

        else:
            print(listEspecie[3]) #vaca

#invertebrados: L26 - L37
elif parametro1 == listTipo[1]:
    if parametro2 == listClasse[2]:
        if parametro3 == listOrdem[3]:
            print(listEspecie[4]) #pulga

        else:
            print(listEspecie[5]) #largata

    elif parametro2 == listClasse[3]:
        if parametro3 == listOrdem[3]:
            print(listEspecie[6]) #sanguessuga

        else:
            print(listEspecie[7]) #minhoca
            