from datetime import datetime
from typing import Optional


class Pessoa:
    def __init__(self, nome: str, data_nascimento: str) -> None:
        self.nome = nome
        self.__data_nascimento = data_nascimento
        self.idade = self.calcular_idade()

    def calcular_idade(self) -> int:
        # Converte a string de data de nascimento para um objeto datetime
        # format = formato da data que eu estou inserindo!
        data_nasc = datetime.strptime(self.__data_nascimento, "%d/%m/%Y")
        # Obtém a data atual
        data_atual = datetime.now()
        # Calcula a idade
        idade = (
            data_atual.year
            - data_nasc.year
            - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day))
        )
        return idade

    def respirar(self) -> None:
        print("Respirando...")


# Pessoa é a superclasse
# Aluno é subclasse de Pessoa
class Aluno(Pessoa):
    def __init__(
        self, nome: str, data_nascimento: str, curso: Optional[str] = None
    ) -> None:
        super().__init__(nome, data_nascimento)
        self.curso = curso

    def calcular_nota(self): ...


class Professor(Pessoa):
    def __init__(self, nome: str, data_nascimento: str, titulacao: str) -> None:
        super().__init__(nome, data_nascimento)
        self.titulacao = titulacao

    def ensinar(self): ...


class FuncionarioPublico(Pessoa):
    def __init__(
        self, nome: str, data_nascimento: str, ferias_premio: Optional[bool] = False
    ) -> None:
        super().__init__(nome, data_nascimento)
        self.ferias_premio = ferias_premio
        self.auxilio_terno = False

    def tirar_abono(self): ...

    def receber_auxilio_terno(self): ...


professor = Professor("Antônio", "06/07/1985", "mestre")  # Argumentos posicionais
aluno = Aluno(data_nascimento="22/01/1991", nome="João")  # Argumentos nominais
func_publico = FuncionarioPublico("José", "06/07/1960", True)
