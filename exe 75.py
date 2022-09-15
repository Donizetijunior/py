#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e 
# guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
num=(int(input('Digite um numero : ')),
    int(input('Digite um numero : ')),
    int(input('Digite um numero : ')),
    int(input('Digite um numero : ')))
print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num :
    print(f'o valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('o numeor 3 nao foi digitado')
for n in num:
    if n%2==0:
        print (n , end=' ')