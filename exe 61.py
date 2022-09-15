# refazer o exe 51 com while.
print('-='*15)
print('OS 10 Termos De uma PA !')
print('-='*15)
primeiro = int(input('Primeiro termo : '))
razao = int(input('Razao da PA : '))
termo= primeiro
cont = 1
while cont <= 10:
    print('{} ¬ '.format(termo),end='')
    termo += razao
    cont += 1
print(' Fim programa !')
