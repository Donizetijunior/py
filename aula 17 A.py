# num=[2,5,9,1]
# num[2]=3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2,2)
# num.remove(2)#remove o primeiro numero
# if 4 in num:
#    num.remove(4)
# else:
#    print('nao tem esse numero')
# num.pop(2)
# print(num)
#print(f'essa  lista tem {len(num)} elementos')
# ---------------------------------------------------------------------------------------
#valores = list()
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for c, v in enumerate(valores):
#    print(f'na posicao {c} tem : {v}....')
# print('Cheguei!')
# ----------------------------------------------------------------------------------------
# valores=list()
# for cont in range(0,5):
#    valores.append(int(input('Digite um valor :  ')))
# print('-'*30)
# for c, v in enumerate(valores):
#    print(f'na posição {c} tem : {v} ')
# print('-'*30)
# ----------------------------------------------------------------------------------------------
# a=[2,3,4,7]
# b=a
# b[2]=8
#print(f'lsita A: {a}')
#print(f'lista B: {b} ')
# --------------------------------------------------------------------------------------------------
A = [4, 5, 6, 7]
b = A[:]  # copiar a lista A
b[2] = 8
print(f'{A}')
print(f'{b}')
