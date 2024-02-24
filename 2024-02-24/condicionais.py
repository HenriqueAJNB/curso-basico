ano = 1900 # Atribuindo o valor 1900 à variável "ano"

# Esse ano é bissexto? Sim ou não!
# O ano é divisível por 4?
# O ano é divisível por 100?
# O ano é divisível por 400?

# if <condicao>:
#    <codigo_a_ser_executado_se_a_condicao_for_verdadeira>

# <condicao> é qualquer coisa que retorne ou True ou False

# Modo 1
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} é bissexto!") # 1
        else:
            print(f"{ano} não é bissexto!") # 3
    else:
        print(f"{ano} é bissexto!") # 2
else:
    print(f"{ano} não é bissexto!") # 4

# Modo 2
if (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é bissexto!") # 1 e 2
else:
    print(f"{ano} não é bissexto!") # 3 e 4

# Modo 3
divisivel_por_4 = ano % 4 == 0
divisivel_por_100 = ano % 100 == 0
divisivel_por_400 = ano % 400 == 0
nao_divisivel_por_100 = not divisivel_por_100

if (
    divisivel_por_4 and 
    divisivel_por_100 and 
    divisivel_por_400
    ) or (
    divisivel_por_4 and 
    nao_divisivel_por_100
):
    print(f"{ano} é bissexto!") # 1 e 2
else:
    print(f"{ano} não é bissexto!") # 3 e 4

# Desafio
nota_media = 7

# A - entre 10 e 7 (inclusos)
# B - entre 6 e 5 (inclusos)
# C - entre 4 e 2 (inclusos)
# D - restante

# Primeira forma, qual é o problema?
if 10 <= nota_media <= 7:
    letra = "A"
if 6 <= nota_media <= 5:
    letra = "B"
if 4 <= nota_media <= 2:
    letra = "C"
else:
    letra = "D"

# Segunda forma, qual é o problema?
if 10 <= nota_media <= 7:
    letra = "A"
if 6 <= nota_media <= 5:
    letra = "B"
if 4 <= nota_media <= 2:
    letra = "C"
if 0 <= nota_media <= 1:
    letra = "D"

# Como resolver?