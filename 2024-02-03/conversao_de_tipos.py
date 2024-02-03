# Transformando número para string!
# num1 = 3
# num2 = 5
# print(type(num1))

# print(num1 + num2, type(num1 + num2))
# 8 (inteiro)

# print(str(num1) + str(num2), type(str(num1) + str(num2)))
# 35 (string)

# print(str(num1 + num2), type(str(num1 + num2)))
# num1 + num2 = 8
# str(num1 + num2) = "8"
# 8 (string)

# Ouras transformações

idade = "32"
peso = "80.7"

# print(int(idade))
peso_arredondado = round(float(peso), 0)
print(peso_arredondado, type(peso_arredondado))
# 80 == 80.0

# int(), str(), float(), bool()
verdadeiro = True # 1
falso = False # 0
string_vazia = ""

print(bool(string_vazia))