# valor da casa  o salario e quantos anos ele vai pagar
#nao pode exceder 30% do salario
valor = float(input('Qual o valor da casa : '))
salario = float(input('Qual o seu salario : '))
anos = int(input('Em quantos anos vai pagar : '))
parcela = valor/(anos*12)
novosal = salario*0.30

if parcela>= novosal:
    print('Emprestimo negado!')
elif parcela <= novosal:
    print('Seu imprestimo foi aprovado ')
    print('parcelas de {:.2f} ao mes  , em {} anos'.format(parcela,anos))