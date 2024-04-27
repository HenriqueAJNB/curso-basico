# import statistics
from collections import Counter

dados = [10, 50, 15, 25, 42]

def media(valores: list[int | float]) -> float:
    return sum(valores) / len(valores)

# print(media(dados))
# print(statistics.mean(dados))

nome = "Henrique Alves Junqueira Nogueira Branco"

contador = {}
for letra in nome:
    if letra not in contador:
        contador[letra] = 1
    else:
        contador[letra] += 1

# Saber qual a letra que mais aparece!
for letra, contagem in contador.items():
    ...

print(f"Solução pura: {contador}\n\n")

# Solução usando collections.Counter
contador = Counter(nome)
print(f"Solução usando Counter: {contador}")

print(f"A letra mais comum é: {contador.most_common(2)}")