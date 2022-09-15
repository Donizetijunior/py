galera=list()
pessoa=dict()
soma=0
while True:
    pessoa.clear()
    pessoa['nome']= str(input('Nome :'))
    while True:
        pessoa['sexo']= str(input('Sexo : [F/M]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade']= int(input('Idade : '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar ?[S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Reponda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)}, pessoa cadastradas !')
media= soma / len(galera)
print(f'A media de idade é de  {media:5.2f} anos ')
print('As mulheres cadastradas    ',end='')
for p in galera:
    if p['sexo']in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(' Lista das pessoas que estao acima da media : ' ,end='')
for p in galera:
    if p['idade']>= media:
        print('         ',end='')
        for k, v in p.items():
            print(f'{k} = {v} ' ,end='')