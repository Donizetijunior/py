#dados =  dict()
#dados = { 'nome' : 'Pedro', 'idade': 25}
#print(dados['nome'])
#dados['sexo'] = 'M'
#print(dados['sexo'])
#del dados['idade']

#filme = {'titulo'  : 'Star Wars',
#'ano' : 1977,
#'diretor': 'george lucas'
#}
#for k , v in filme.items():
#    print(f'O {k} é {v}')

#-----------------------------------------------------------------------------

#pessoas = {'nome' : ' Gustavo', 'sexo'  : 'M', 'idade' : 22}
#print (f'o {pessoas["nome"]} tem {pessoas["idade"]} ')
#print(pessoas.items())
#pessoas['nome'] = 'Leandro'  # -- >  está adicionando ou mudando o nome 
#for k, v  in pessoas.items():
#    print(k , v)

#------------------------------------------------------------------------------
#brasil = [] # -> lista
#estado1 = {'uf': 'Rio de Janeiro' , 'sigla' : 'RJ'}
#estado2 = {'uf' : 'São paulo', 'sigla' : 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print (brasil[1]['sigla'])

#---------------------------------------------------------------------------------
estado =  dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa : '))
    estado['sigla']= str(input('Sigla do Estado : '))
    brasil.append(estado.copy())
for e in brasil :
    for v in e.values():
        print(v, end='  ')
    print()