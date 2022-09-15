#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = [] 
par = []
impar = []
while True:
    n= int(input('Digite um valor : '))
    lista.append(n)
    
    if n %2 == 0 :
        par.append(n)
    elif n %2 ==1 :
        impar.append(n)
    resp = str(input('Quer continuar ? [S / N ]'))
    if resp in 'Nn':
        break 

print(f' lista com todos os valores {lista}')
print(f' lista com todos os valores pares {par}')
print(f' lista com todos os valores  impares {impar}')



