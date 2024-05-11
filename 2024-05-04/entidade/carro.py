from entidade.pessoa import Pessoa


class Carro:
    def __init__(
        self, capacidade_tanque: int, autonomia_km: int, tracao_4x4: bool
    ) -> None:
        self.capacidade_tanque = capacidade_tanque
        self.autonomia_km = autonomia_km
        self.tracao_4x4 = tracao_4x4
        self.quilometragem = 0
        self.passageiros: list[Pessoa] = []

    def viajar(self, distancia: int) -> None:
        self.quilometragem += distancia

    def fazer_primeira_manutencao(self) -> bool:
        return self.quilometragem >= 10_000

    def adicionar_passageiro(self, passageiro: Pessoa) -> None:
        self.passageiros.append(passageiro)

    def remover_todos_passageiros(self) -> None:
        self.passageiros = []
