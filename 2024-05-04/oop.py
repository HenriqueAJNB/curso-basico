from entidade.carro import Carro
from entidade.pessoa import Pessoa

carro_1 = Carro(45, 900, True)

p1 = Pessoa("João", 21)
p2 = Pessoa("Arthur", 30)

carro_1.adicionar_passageiro(p1)
carro_1.adicionar_passageiro(p2)

carro_1.remover_todos_passageiros()

soma_idades = sum([p.idade for p in carro_1.passageiros])
print(soma_idades)
