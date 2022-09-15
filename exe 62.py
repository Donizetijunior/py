# melhore o 61 e peça se ele quer mais termos da PA  termina com 0]
print('-='*15)
print('OS 10 Termos De uma PA !')
print('-='*15)
primeiro = int(input('Primeiro termo : '))
razao = int(input('Razao da PA : '))
termo= primeiro
cont = 1
total= 0
mais = 10
while mais != 0 :
    total+= mais
    while cont <= total :
        print('{} ¬ '.format(termo), end='')
        termo += razao
        cont += 1
    print(' pausa !')
    mais=int(input('Quantos termos voce quer a mais ? '))
print('Progressao finalizada com {} termos mostrados !'.format(total))