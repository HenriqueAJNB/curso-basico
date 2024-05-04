# Exercício 3:
# Um determinado zoológico cobra a entrada com base na idade do visitante. Os visitantes com 2 anos de idade ou menos não pagam para entrar. Crianças entre 3 e 12 anos custa R$14,00. Idosos com 65 anos ou mais custam R$18,00. A entrada para todos os outros visitantes é de R$23,00. Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, com uma idade inserida em cada linha. O usuário digitará uma linha em branco para indicam que não há mais visitantes a serem inseridos.

valores_ingressos = []
idade = input("Digite aqui a idade do visitante (aperte enter para encerrar): ")

while idade:
    idade = int(idade)

    if idade < 0:
        raise ValueError("Idade deve ser igual ou superior à 0!")

    if idade >= 0 and idade <= 2:
        ingresso = 0
    elif idade >= 3 and idade <= 12:
        ingresso = 14
    elif idade >= 65:
        ingresso = 18
    else:
        ingresso = 23
    valores_ingressos.append(ingresso)

    idade = input(
        "Digite aqui a idade do outro visitante (aperte enter para encerrar): "
    )
    # sum(valores_ingressos) -> int
valor_devido = round(sum(valores_ingressos), 2)
# round(2,5) -> 2
print(f"O valor a ser pago pelo grupo é de R${valor_devido:.2f}".replace(".", ","))
