#contagem regressiva para 10 a 0 e um delay(1)
from time import  sleep
for i in range(10,0,-1):
    print(' Faltam {}'.format(i))
    sleep(1)
print(' Fim ! ')