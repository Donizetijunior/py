# parada com 999 , mostrar quantos numeros foram inseridos e qual a soma deles.
n = 0
cont = 0
novo = 0
n = int(input('Digite o {} numero [999 para parar] :'
              '>'.format(n)))
while n != 999 :
        novo += n
        cont += 1
        n=int(input('digite um numero [999 para parar]:'))
print('Voce inseriu {} numeros e a soma dele é {} '.format(cont,novo))