from __future__ import annotations  # Usar a classe como anotação de tipo


# DEFINIÇÃO
class Conta:
    def __init__(self, nr: str, saldo_inicial: float) -> None:
        self.__nr = nr  # Atributo público
        self.__saldo = saldo_inicial  # Atributo privado (acesso de leitura!)
        # __saldo vira _Conta__saldo

    @property
    def nr(self):
        return self.__nr

    @property
    def saldo(self):
        return self.__saldo

    def sacar(self, valor: float) -> None:
        if valor > self.__saldo:
            raise ValueError("Saldo indisponível.")
        self.__saldo -= valor

    def depositar(self, valor: float) -> None:
        self.__saldo += valor

    def transferir(self, conta_destino: Conta, valor: float) -> None:
        if valor > self.__saldo:
            raise ValueError("Saldo indisponível.")
        self.__saldo -= valor
        conta_destino.__saldo += valor


# USO
c1 = Conta("0001", 0)
c2 = Conta("0002", 1_000)

c1.depositar(10_000)
print(f"Saldo c1 após deposito: {c1.saldo}")
c2.sacar(100)
print(f"Saldo c2 após saque: {c2.saldo}")
c1.transferir(c2, 50)
print(f"Saldo c1 após transferência: {c1.saldo}")
print(f"Saldo c2 após transferência: {c2.saldo}")

# Fere a separação entre definição e uso!

# self.__saldo -> não cria o atributo __saldo
# self.__saldo -> cria um atributo chamado _Conta__saldo

# Mas ainda sim eu consigo modificá-lo
# c1.__saldo = 10_000
# print(type(c1))

# Atributo 1 -> _Conta__saldo criado na inicialização da classe e tem valor 0
# Atributo 2 -> __saldo criado fora da classe com valor 10_000

# Não tenho acesso ao atributo de saldo
# print(c1.__saldo)
