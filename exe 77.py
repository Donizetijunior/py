#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras 
# (não usar acentos). Depois disso, você deve mostrar, 
# para cada palavra, quais são as suas vogais
palavras=('abecedario','acucar','programar','buceta','prostituta')
for p in palavras:
    print(f'\n Na palavra {p} temos ', end=' ')
    for letra in p :
        if letra.lower() in 'aeiou':
            print(letra , end =' ')