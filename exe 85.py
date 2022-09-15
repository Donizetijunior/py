#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
valor =0 
for c in range(0,7):
    valor = int(input('Digite um valor : '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor  % 2 ==1 :
        numeros[1].append(valor)
print('-'*30)
numeros[0].sort()
numeros[1].sort()
print(f'os valores pares foram {numeros[0]}')
print(f'os valores impares sao {numeros[1]}')