# triangulos
print('Classificação de triangulos !')
n1=int(input('Digite o primeiro numero :'))
n2=int(input('Digite o segundo numero : '))
n3=int(input('Digite o terceiro numero :'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1+n2:
    print('Os seguimentos podem formar um triangulo : ',end='')
    if n1 == n2 ==  n3 :
        print('EQUILATERO !')
    elif n1 != n2 != n3 != n1 :
        print('ESCALENO !')
    else:
        print('ISOSCELES !')
else:
    print('Não formam um triangulo !')
