#media , ler duas notas e calcular a media
print('Sistema para ver as medias ! ')
nota1=float(input('Digite a nota 1 : '))
nota2=float(input('Digite a nota 2 : '))
media = (nota1+nota2)/2
if media >= 70:
    print('Aprovado ! ')
elif media >= 50 and media <= 69:
    print('Em Recuperação !')
elif media < 50:
    print('Reprovado ! ')