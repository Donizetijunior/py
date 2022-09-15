# jogador tem que acertar um numero escolhido pelo pc de 0 a 10 ate acertar
from random import randint
computador = randint(0,10)
palpite = 0
print('Sou seu computador ... estou pensando em um numero de 0 a 10 :p')
print('Tente acertar :D!')
acertou = False
while not acertou:
    jogador=int(input('Qual seu palpite : '))
    palpite+=1
    if jogador == computador:
            acertou = True
    else:
        if jogador < computador:
            print('Mais ... tente de novo !')
        elif jogador>computador:
            print('Menos... Tente de novo !')

print('Acerto miseravi , com {} tentativas  ! '.format(palpite))