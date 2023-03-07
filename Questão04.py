dic = {
    'SP':67836.43, 'RJ':36678.66, 'MG':29229.88, 'ES':27165.48, 'Outros':19849.53
}
total = 0
for valor in dic.values():
    total += valor
sp = dic['SP']/total
rj = dic['RJ']/total
mg = dic['MG']/total
es = dic['ES']/total
outros = dic['Outros']/total
print(f'São Paulo possuiu {sp*100:.2f}% de representação no valor total da distribuidora!!')
print(f'Rio de Janeiro possuiu {rj*100:.2f}% de representação no valor total da distribuidora!!')
print(f'Minas Gerais possuiu {mg*100:.2f}% de representação no valor total da distribuidora!!')
print(f'Espírito Santo possuiu {es*100:.2f}% de representação no valor total da distribuidora!!')
print(f'Outros Estados possuíram {outros*100:.2f}% de representação no valor total da distribuidora!!')