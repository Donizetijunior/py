# ler um numero qualquer e mostar seu Fatorial !
''''#from math import factorial
n=int(input('Digite o numero que deseja o fatorial '
            '>>>'))
f= factorial(n)
print('O fatorial de {} é {} '.format(n,f))'''

n = int(input('Digite o numero que deseja o fatorial '
            '>>>'))
f = 1
i = n
print('Calculando {}! =  '.format(n),end='')
while i > 0 :
    print('{}'.format(i),end='')
    print(' x 'if i > 1 else '= ',end='')
    f = f * i
    i -= 1
print(' {}'.format(f))



