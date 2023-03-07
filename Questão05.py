def reversao(string):
    resultado = ''
    for c in range(len(string)-1, -1, -1):
        resultado += string[c]
    return resultado

entrada = input('Informe a palavra ou frase desejada para ser invertida: ')
print(reversao(entrada))