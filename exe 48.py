soma = 0
cont = 0
for i  in range(1,501,2):
    if i %3==0:
        cont += 1
        soma += i
print('a soma de  todos os {} valore é {} '.format(cont,soma))