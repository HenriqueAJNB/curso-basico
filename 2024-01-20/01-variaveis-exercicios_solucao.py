# Calcula a área (em m²) de uma sala com dimensões 
# 3m (largura) x 4m (comprimento). Imprima o resultado na tela.
# Escrever o código abaixo
largura = 3
comprimento = 4
area = largura * comprimento
print(area)

# Calcula o volume (em litros) de uma piscina com dimensões 
# 4m (largura) x 5m (comprimento) x 2m (profundidade). Imprima o resultado na tela
# Escrever o código abaixo
largura = 4
comprimento = 5
profundidade = 2
# mil: 1.000 (pt-br) ou 1,000 (en)
m3_para_litros = 1_000
volume = largura * comprimento * profundidade * m3_para_litros
print(volume)

# Solução usando funções
def calcula_area(largura, comprimento):
    area = largura * comprimento
    return area

# function blablabla(): 
#   
# 
def calcula_volume(largura, comprimento, profundidade):
    m3_para_litros = 1_000
    volume = largura * comprimento * profundidade * m3_para_litros
    return volume

print(calcula_area(4, 5))
print(calcula_volume(4, 5, 2))