#programa para ler 2 valores e mostrar um menu na tela de soma
num1=int(input('Digite o primeiro valor : '))
num2=int(input('Digite o segundo valor : '))
opcao=0
while opcao !=5 :

    opcao = int(input('''Escolha o que deseja fazer :
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NUMERO
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA
                          >>> '''))

    if opcao ==1 :
        print('A soma é >>> {}  '.format((num1+num2)))

    elif opcao == 2:
        print('A multiplicação é >>> {} '.format(num1*num2))
    elif opcao == 3:
        if num1 > num2:
            print(' numero 1 é o maior {} '.format(num1))
        if num2 > num1:
            print(' numero 2 é maior {} '.format(num2))
    elif opcao == 4 :
        print('Digite os novos numeros : ')
        num3 =int(input('Digite o primeiro valor : '))
        num1 = num3
        num4 = int(input('Digite o segundo valor : '))
        num2 =num4
print('Fim do programa ! ')