
#teste= list()
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0]= 'Maria'
#teste[1] = 20
#galera.append(teste[:])
#print(galera)
#------------------------------------------------------------------------

#galera= [['Joao',19], ['Ana',33], ['Joaquim',32], ['Maria',99]]
#print(galera[1][0])

#---------------------------------------------------------------------

#galera= [['Joao',19], ['Ana',33], ['Joaquim',32], ['Maria',99]]
#for p in galera:
#    print(f'´{ p[0] }tem {p[1]} anos !')

#------------------------------------------------------------------------

galera = list()
dado = list()
maior=menor=0
for c in range (0,3):
    dado.append(str(input('Nome : ')))
    dado.append(int(input('Idade : ')))

    galera.append(dado[:])
    dado.clear()
    
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade !' )
        maior+=1
    else:
        print(f'{p[0]} é menor de idade !')
        menor+=1
print(f'Temops {maior} maiores e {menor} menores de idade !')
