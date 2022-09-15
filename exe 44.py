print('Mercadinho da Berenice ! ')
preco=float(input('Qual é o preço a ser cobrado :   >'))
print(''' Escolha a forma de pagamento :
        [1] á Vista dinheiro ou cheque com 10% de desconto . 
        [2] a Vista no cartão com 5% de desconto .
        [3] em até 2x no cartão com o preço normal .
        [4] 3x ou mais no cartão com 20% de juros.''')
opcao = int(input(' Sua escolha : '))
if opcao ==1:
    print(' o valor R${} , ficara por : R${} '.format(preco,preco-(preco*0.10)))
elif opcao ==2:
    print('O valor R${} ficara por : R${} '.format(preco,preco-(preco*0.05)))
elif opcao ==3:
    parcela=preco/2
    print('O valor ficara R${} em 2x de R${}'.format(preco,parcela))
elif opcao==4:
    parcelas=int(input('Em quantas parcelas:'))

    preconovo=preco+(preco*0.20)
    parcela = preconovo / parcelas
    print('O preco R${} ficara por : R${} em  {}x  de R${}'.format(preco,preconovo,parcelas,parcela))
else:
    print('Opcao invalida !')