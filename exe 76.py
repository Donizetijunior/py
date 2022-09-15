#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
#  e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

listagem=('lapis',1.73, 'borracha',1.00,'livro',3.30,'capa',9.00)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(listagem)):
    if pos %2==0:
        print(f'{listagem[pos]:.<30}',end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)