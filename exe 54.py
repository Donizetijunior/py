from datetime import date
atual = date.today().year
contm = 0
contn = 0
for i in range(1,8):
    ano=int(input('Digite o ano de nascimento da {}º pessoa : > >  '.format(i)))
    idade = atual - ano
    if idade >= 18:
        contm += 1
    else:
        contn += 1
print(' > {}  pessoas são maior de idade !'.format(contm))
print(' > {}  pessoas são menor de idade !'.format(contn))
