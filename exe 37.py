num=int(input('numero iteiro : '))
print('''escolha uma das bases para conversão :
      [1] converter para Binario
      [2] converter para Octal
      [3] converter para Hecadecimal ''')
opcao= int(input('sua escolha  : '))
if opcao == 1 :
    print(' {} convertido para binario é {} '. format(num,bin(num)[2:]))
elif opcao == 2:
    print(' {}  convertido para octal é {} '.format(num,oct(num)[2:]))
elif opcao == 3:
    print(' {} convertido  para hexadecimal é {} '.format(num,hex(num)[2:]))
else :
    print('opção invalida tente novamente !')
