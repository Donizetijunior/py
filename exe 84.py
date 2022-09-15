#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,  
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
tempo = []
princ = []
maior=menor=0

while True:
    tempo.append(str(input('Nome : ')))
    tempo.append(int(input('Peso : ')))

    if len(princ) == 0:
        maior = menor = tempo[1]
    else:
        if tempo[1] > maior :
            maior = tempo[1]
        if tempo[1] < menor:
            menor = tempo[1]

    princ.append(tempo[:])
    tempo.clear()
    resp= str(input('Quer continuar ? [ S / N ] '))
    if resp in 'Nn':
        break

print('-'*30)
print(f'Os dados foram {princ} \n')
print(f'Foram cadastradas {len(princ)} pessoas  ! \n') # A)
print(f'O maior peso foi {maior} KG',end= ' ')
for p in princ:
    if p[1]== maior:
        print(f'{p[0]} ', end=' ')
print(f'O menor peso foi {menor} KG',end=' ')
for p in princ:
    if p[1]== menor:
        print(f'{p[0]} ', end=' ')
