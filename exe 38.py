num1=int(input('digite o primeiro numero : '))
num2=int(input('digite o segundo numero : '))

if num1 > num2:
    print('Numero 1  = {} é maior que numero 2 = {} '.format(num1,num2))
elif num2 > num1:
    print('Numero 2 = {} é maior que o numeor 1 = {} '.format(num2,num1))
elif num1 == num2:
    print('os dois numeros são iguais ! ')
