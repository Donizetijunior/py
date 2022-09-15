nome=str(input('qual é o seu nome ? '))
if nome == 'gustavo':
    print('que nome bonito')
elif nome == 'Pedro'or nome == 'Maria':
    print('seu nome é normal')
elif nome in 'Ana Claudia Jessica':
    print('Belo nome')
else:
    print('seu nome  é ruim')
print('tenha um bom dia {}'.format(nome))