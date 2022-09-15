# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use 
# parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
# abertos e fechados na ordem

exp = str(input('Digite sua expressão :  '))
achado=[]
for simb in exp:
    if simb == '(':
        achado.append('(')
    elif simb == ')':
        if len(achado) > 0:
            achado.pop()
        else:
            achado.append(')')
            break
if len(achado) == 0 :
    print(' sua expressao esta  ok!')
else:
    print('Deu erro !')