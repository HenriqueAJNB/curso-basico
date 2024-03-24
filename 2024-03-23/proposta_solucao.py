# Modificações na quantidade de notas disponíveis:
notas_disponiveis = {
    10: 10_000,
    20: 10_000,
    50: 5_000,
    100: 2_000,
    200: 500,
}

# 10, 20, 50, 100, 200 (combinações de apenas 1 nota)
# 30, 60, 110, 210, ... (combinações de 2 nota)
# 80, ... (combinações de 3 nota)
# 180, ... (combinações de 4 notas)
# 280, ... (combinação de 5 notas)

valor_saque = 30
# Todas combinações possíveis
# Combinações 30
# [[(3,10)],[(1,20), (1,10)]]
# Combinações 40
# [[(4,10)],[(2,10), (1,20)], [(2,20)]]
nota_minima_disponivel = min(notas_disponiveis.keys())

if nota_minima_disponivel > valor_saque or valor_saque % nota_minima_disponivel != 0:
    raise ValueError("Valor não pode ser sacado!")

combinacoes = []
notas_abaixo_saque = {
    nota:quantidade 
    for nota, quantidade in notas_disponiveis.items()
    if nota <= valor_saque
}

for nota in notas_abaixo_saque:
    if valor_saque % nota == 0:
        combinacoes.append([(valor_saque //nota, nota)])
print(combinacoes)