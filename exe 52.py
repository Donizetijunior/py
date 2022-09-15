#ler um numero inteiro e dizer se é primo ou nao :
num=int(input('Digite um numero inteiro : '))
cont = 0
for i in range(1,num+1):
    if num % i:
        print('\033[33m',end=' ')
        cont += 1
    else:
        print('\033[31m',end=' ')
    print('{} '.format(i))

print('\033[m o numero {} foi divisivel {} vezes . '.format(num,cont))
if cont == 2:
    print('Ele é primo! ')
else:
    print('Não é primo ! ')
