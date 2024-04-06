# Funções!
def media(valores: list[int | float]) -> float:
    return round(sum(valores) / len(valores), 2)


# valores1 = [2, 4, 5, 7, 8, 9]
# valores2 = [5, 4, 10, 47, 58, 49]
# valores3 = [3, 40.5, 30, 70, 48, 59]
# valores4 = [6, 10, 5.0, 17, 87, 99, 10]

# media1 = media(valores1)
# media2 = media(valores2)
# media3 = media(valores3)
# media4 = media(valores4)

# print(media1, media2, media3, media4)
# print("Olá mundo!")

# Retorno vs não retorno
valores = [2, 4, 5, 7, 8, 9]
valores.append(30)
valores2 = valores.copy()
print(valores)

nome = "Henrique Alves"
nome_alterado = nome.lower().replace("Henrique", "João")
nome.split()
print(nome_alterado)
