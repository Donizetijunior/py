# alistamento militar
print('Alistamento para o Exercito de MEMES')
idade=int(input('Digite o ano de nascimento : '))

ano =  2022-idade

if ano == 18:
    print('Você deve se alistar !')
elif ano > 18:
    print('Você já deveria ter se alistado há {} ano(s)'.format(ano-18))
elif ano < 18:
    print('Você ainda não podera se alistar falta  {} ano(s) '.format(18-ano))