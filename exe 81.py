# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre: A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0
while True:
    n=int(input('Digite um numero :  '))
    lista.append(n)
    cont +=1
    r = str(input('Quer continuar ?  [s\ n]'))
    if r in 'Nn':
        break
print (f'Total de numeros digitados : {cont} ')
lista.sort(reverse=True)
print(f' decrescente : {lista}')
if 5 in lista:
    print('o numero 5 esta na lista')
else:
    print('o numero 5 nao esta na lista')