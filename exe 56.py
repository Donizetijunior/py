somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho  = 0
mulher20 = 0

for i in range(1,5):
    print('-------- {}º Pessoa -------'.format(i))
    nome=str(input('Nome : ')).upper()
    idade=int(input('Idade : '))
    sexo=str(input('Sexo [F ou M] : ')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediaidade = somaidade /4
print('A media de idade do grupo é {:.2f} '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos .'.format(mulher20))
