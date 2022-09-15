#Funções
#def mostralinha():
#    print('-'*30)
#def titulo(txt):
#    print('-'*40)
#    print(txt)
#    print('-'*40)
#titulo('Curso de Py')
#titulo('Py é delicia !')
#----------------------------------------------------
#def soma(a, b):
#    print(f' A = {a} e B= {b}')
#    s = a + b
#    print(f'Soma dos numeros é  {s}')


#soma(1, 5)
#soma(1, 11)
#soma(5, 520)

#-------------------------------------------------------
#empacotamento :
#def contador(*num):
#    tam= len(num)
#    print(f'{tam} ')


#contador(2, 1, 9)
#contador(4, 6, 6, 9, 7, 5)
#----------------------------------------------------
#def dobra(lst):
#    pos=0
#    while pos < len(lst):
#        lst[pos]*=2
#        pos+=1
#
#valores=[9,9,1,5,8,6]
#dobra(valores)
#print(valores)

#----------------------------------------------------
def soma (* valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(15, 55)