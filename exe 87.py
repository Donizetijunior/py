#Exercício Python 087: Aprimore o desafio anterior, mostrando no final : 
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
somap= maior =somacol=0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor  para a posição [{l}, {c}] :'))

print()
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
   
        if matriz[l][c] %2 ==0:#A)
            somap+=matriz[l][c]
    print()
for l in range(0,3):
    somacol+= matriz[l][2]
for c in range(0,3):
    if c == 0 :
        maior= matriz[1][c]
    elif matriz[1][c]>maior:
        maior=matriz[1][c]

    
print('-'*30)
print(f'A soma dos valores pares : {somap}')
print(f'A soma dos valores da terceira coluna é  : {somacol}')
print(f'O maior numero da segunda coluna é : {maior}')
print()
