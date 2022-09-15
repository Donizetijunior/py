print('OS 10 Termos De uma PA !')

n1 = int(input('Qual é o primeiro termo da PA : '))

r = int(input('Qual é a razão da PA : '))

decimo = n1+(10-1)*r

for i in range(n1 , decimo + r , r):

    print('{}' .format(i), end = '¬ ')

print('FIM! ')