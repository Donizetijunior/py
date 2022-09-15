#saber se é uma frase  palidroma
frase=str(input('Digite uma frase : ')).strip().upper()

palavras = frase.split()

junto = ''.join(palavras)

inverso = ''
#inverso = junto[::-1] #sem o for !
for letra in range(len(junto)-1, -1, -1):# com for !
        inverso += junto[letra]
print('O inverso de {} é {} '.format(junto,inverso))
if inverso ==junto:

    print('Temos um palindromo!')

else:

    print(' a frase digitada nao é um palidromo!')
