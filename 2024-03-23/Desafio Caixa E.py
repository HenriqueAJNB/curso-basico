# Resolução exercício saque cédulas João Felipe!


def distribuir_notas(valor_saque):
    # Lista de notas disponíveis no caixa eletrônico
    notas_disponíveis_no_caixa_eletrônico = [200, 100, 50, 20, 10]
    # Lista com o valor da cédula e a quantidade disponíveis
    total_de_notas_disponiveis_por_cedula = [
        (200, 500),
        (100, 2000),
        (50, 5000),
        (20, 10000),
        (10, 10000),
    ]
    notas_utilizadas = []

    # Verificar se o saque é válido (mínimo de 10 reais e múltiplo de 10)
    if valor_saque < 10 or valor_saque % 10 != 0:
        return "Valor de saque inválido. O saque deve ser de pelo menos 10 reais e múltiplo de 10."

    # Limitar notas de 10 reais para saques abaixo de 100 reais
    if valor_saque < 100:
        max_cedulas_10_reais = 3
    else:
        max_cedulas_10_reais = 0

    for (
        notas_disponíveis_no_caixa_eletrônico,
        quantidade_disponivel,
    ) in total_de_notas_disponiveis_por_cedula:
        # Limitar uso de notas de 10 reais
        if (
            notas_disponíveis_no_caixa_eletrônico == 10
            and len(notas_utilizadas) >= max_cedulas_10_reais
        ):
            continue

        while (
            valor_saque >= notas_disponíveis_no_caixa_eletrônico
            and quantidade_disponivel > 0
        ):
            notas_utilizadas.append(notas_disponíveis_no_caixa_eletrônico)
            valor_saque -= notas_disponíveis_no_caixa_eletrônico
            quantidade_disponivel -= 1

    if valor_saque != 0:
        return "Não é possível sacar este valor com as notas disponíveis."
    else:
        return notas_utilizadas


resposta = "sim"

saldo = 2500

while resposta == "sim":
    valor_saque = int(input("Quanto deseja sacar? "))
    if valor_saque <= saldo:
        distribuir_notas(valor_saque)
        saldo = saldo - valor_saque
        print(f"Saldo atual é: {saldo}")
    else:
        print("Operação não autorizada")

    resposta = input("Deseja realizar outra operação? [sim/nao] ")
