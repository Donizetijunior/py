from random import randint
from time import  sleep

itens = ( 'Pedra','Papel', 'Tesoura')

computador = randint(0,2)

print(''' Suas opções :
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador=int(input('Qual é sua Jogada ?   > '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !')
sleep(1)

print('-=' * 19)
print('O Jogador escolheu    : {}'.format(itens[jogador]))
print('O computador escolheu : {} '.format(itens[computador]))
print('-=' * 19)

if computador == 0:
    if jogador == 0:
        print('Empate !')
    elif jogador ==1:
        print('Jogador Perdeu !')
    elif jogador ==2:
        print('Jogador Ganhou !')
    else:
        print('Jogada invalida !')

elif computador ==1:
    if jogador == 0:
        print('Jogador Perdeu !')
    elif jogador ==1:
        print('Empate !')
    elif jogador ==2:
        print('Jogador Ganhou !')

    else:
         print('Jogada invalida !')


elif computador ==2:
    if jogador == 0:
        print('Jogador Ganhou !')
    elif jogador ==1:
        print('Jogador Perdeu !')
    elif jogador ==2:
        print('Empate !')
    else:
         print('Jogada invalida !')