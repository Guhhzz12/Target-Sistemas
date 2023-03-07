n = int(input('Digite o valor que deseja encontrar: '))
primeiro = 0
fibonacci = 1
aux = 0
flag = False
while fibonacci <= n:
    aux = fibonacci
    fibonacci += primeiro
    primeiro = aux
    if fibonacci == n:
        flag = True
        break

if flag == True:
    print('O número informado pertence à sequência de fibonacci!!!')
else:
    print('O número informado não pertence à sequência de fibonacci!!!')
