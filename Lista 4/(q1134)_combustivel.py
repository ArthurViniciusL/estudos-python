type_combust = int(input())

alcool = 0 ; gasolina = 0 ; diesel = 0 

while type_combust != 4:

    if type_combust == 1:
        alcool += 1
    elif (type_combust == 2):
        gasolina += 1
    
    elif (type_combust == 3):
        diesel += 1

    type_combust = int(input())

print("MUITO OBRIGADO")
print("Alcool: %i\nGasolina: %i\nDiesel: %i"
%(alcool, gasolina, diesel))