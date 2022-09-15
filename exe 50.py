#soma dos numeros pares.
cont = 0
soma = 0
for i in range(1,7):
    num=int(input('Digite o {} valor : '.format(i)))
    if num  % 2  == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi de {} !'.format(cont,soma))