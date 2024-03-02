# Desafio
nota_media = 12

# A - entre 10 e 7 (inclusos)
# B - entre 6 e 5 (inclusos)
# C - entre 4 e 2 (inclusos)
# D - restante

# Primeira forma, qual é o problema?
# 1. Erro nas condições!
# 2. Usar elif ao invés de if (aceitar apenas uma condição!)
# if 7 <= nota_media <= 10:
#     letra = "A"
# elif 5 <= nota_media <= 6:
#     letra = "B"
# elif 2 <= nota_media <= 4:
#     letra = "C"
# else:
#     letra = "D"
# print(letra)

# Segunda forma, qual é o problema?

if not 0 <= nota_media <= 10:
    raise ValueError("Nota inválida. A nota deve ser entre 0 e 10!")

if 7 <= nota_media <= 10:
    letra = "A"
elif 5 <= nota_media <= 6:
    letra = "B"
elif 2 <= nota_media <= 4:
    letra = "C"
elif 0 <= nota_media <= 1:
    letra = "D"

print(letra)
