nome = "Henrique Alves Junqueira Nogueira Branco"

# Como calcular o comprimento de uma string?
# Quantos caracteres eu tenho?
# len(" ") = Calcula quantos caracteres eu tenho na string " "
# print(len(nome) - len(" "))
# 40 - 1 = 39

# Como contar quantos caracteres eu tenho sem contabilizar espaços em branco?
# Forma 1:
# print(len(nome.replace(" ", "")))
# 36

# Forma 2:
# print(len(nome) - nome.count(" "))
# 36

# Forma 3: usando for
# Forma 4: usando alfabeto completo
# Forma 5: ...

# Porque len(nome) e não nome.len()?
# O que seria len() e o que seria str.len()?
# precos = [10, 12, 15]

# print(len(precos))
# 3

# Como conseguir apenas o primeiro nome?
print(type(nome.split(" ")))

print(3 + 5)
print("3" + "5")
