#so aceita F ou M , tente ate acertar
#inicio de validação

sexo = str(input('Informe o seu Sexo [F/M] : ')).upper()[0].strip()

while sexo not in 'MF':
    sexo = str(input('Dados invalidos ! insira novamente , Informe o seu Sexo [F/M] :')).upper()[0].strip()
print('Sexo {} registrado com sucesso !'.format(sexo))



