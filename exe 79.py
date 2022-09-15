#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
#  cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = list()
while True:
    n=int(input('Digite um valor :  '))
    if n not in numeros:
        numeros.append(n)
        print('adicionado com sucesso!')
    else:
        print('valor duplicado!')
    r = str(input('Quer continuar ?  [s\ n]'))
    if r in 'Nn':
        break
print('-'*33)
numeros.sort()
print(f'voce digitou os valores {numeros}')