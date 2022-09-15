print('Calculando o IMC de uma pessoa !')
altura=float(input('Digite a Altura : '))
peso=float(input('Digite o Peso : '))
imc=peso/(altura*altura)
if imc<=18.5:
    print('Abaixo do peso ! ')
elif imc >18.5 and imc <=25:
    print('Peso ideal  IMC : {:.2f} ! '.format(imc))
elif imc > 25 and imc <=30:
    print('Sobrepeso  IMC : {:.2f} ! '.format(imc))
elif imc>30 and imc <= 40:
    print('Obesidade IMC : {:.2f} ! '.format(imc))
elif imc > 40:
    print('Obesidade Mórbida IMC : {:.2f}, Cuidado  ! '.format(imc))