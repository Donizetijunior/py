# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e
   # o menor valor digitado e as suas respectivas posições na lista.
listanum = []
maior= 0
menor= 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c ==0 :
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor :
            menor = listanum[c]

print('-'*30)
print (f'vode digitou ois valores {listanum}')
print(f'o maior numero digitado foi : {maior} nas posições ', end = '')
for i,v in enumerate(listanum):
    if v == maior:
        print (f'{i}...', end = '')

print(f'o menor numero digitado foi : {menor} nas posições ', end = '')
for i,v in enumerate(listanum):
    if v == menor:
        print (f'{i}...', end = '')

