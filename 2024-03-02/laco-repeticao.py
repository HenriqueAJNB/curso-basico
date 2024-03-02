# CONCEITO!
# laço for
#   - sei quantas vezes o código repetido será executado
# laço while
#   - NÃO SEI quantas vezes o meu código vai ser executado
#   - Vai ou não ser executado baseado em uma condição!

# SINTAXE
# for <variavel> in <sequencia>:
#     <codigo-a-ser-executado>
#     código pode usar a variável aqui!

sequencia = [1, 2, 3, 4]

for elemento in sequencia:
    print(elemento)

nome = "Henrique Alves Junqueira"

for letra in nome:
    print(letra)

for parte_nome in nome.split():
    print(parte_nome)

# H
# He
# Hen
# Henr
# ...

for posicao in range(len(nome)):
    print(nome[: posicao + 1])

# for posicao, _ in enumerate(nome, start=1):
#     print(nome[:posicao])

meses = ["janeiro", "fevereiro", "março", "abril"]
#        0           1             2

for posicao in range(len(meses)):
    print(f"O mês de {meses[posicao]} é o {posicao + 1} do ano")

for nr_mes, nome_mes in enumerate(meses, 1):
    print(f"O mês de {nome_mes} é o {nr_mes} do ano")
