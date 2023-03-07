import json

with open('faturamento.json') as file:
    data = json.load(file)

vetor = [dia['valor'] for dia in data['dias']]

menor = min(vetor)
maior = max(vetor)

faturamento = [dia['valor'] for dia in data['dias'] if dia['valor'] > 0]
media = sum(faturamento) / len(faturamento)

acima = sum(1 for valor in faturamento if valor > media)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {acima}")
