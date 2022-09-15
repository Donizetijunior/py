from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento : '))
idade = atual-nascimento
print('O atleta tem {} anos'.format(idade))
if idade <=9:
    print('Classificação : MIRIM !')
elif idade <=14:
    print('Classificação : INFANTIL !')
elif idade <=19:
    print('Classificação : JUNIOR !')
elif idade <= 25:
    print('Classificação : SENIOR !')
else:
    print('Classificação : MASTER !')





#print('Confederação Nacional de natação !' )
#idade=int(input('Digite o ano de nascimento : '))
#ano = 2022 - idade
#print('O atleta tem {} anos '.format(ano))
#if ano <= 9 :
#    print('MIRIM ! ')
#elif ano > 9 and ano <=14:
#    print('INFANTIL ! ')
#elif ano > 14 and ano <=19 :
#    print('JUNIOR ! ')
#elif ano > 19 and ano <=25:
#    print('SENIOR ! ' )
#elif ano > 25:
#    print('MASTER ! ')