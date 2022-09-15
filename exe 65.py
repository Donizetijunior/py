#programa deve perguntar a hora da parada
#receber numeros inteiro e fazer a media de todos inseridos
# e mostar o maior e o menor numero
opcao = ''
cont = quant = maior = menor = soma = 0
while opcao != 'N':
    num=int(input('Digite  o {} numero :  '
                '>  '.format(quant+1)))
    quant+=1
    cont+=num
    opcao=str(input('Deseja continuar ? [S/N]'
                    '>  ')).upper()
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


media = cont/quant
print('A soma de todos os numeros digitados {} e a media {}  !'.format(cont,media))
print('O maior valor {} e o menor valor {} '.format(maior,menor))