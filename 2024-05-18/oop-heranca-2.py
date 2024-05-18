from statistics import mean

lista = list(1, 2, 3, 4)
media = mean(lista)


class MinhaLista(list):
    def __init__(self, *args):
        super().__init__(*args)

    def calcula_media(self):
        return sum(self) / len(self)


list(1, 2, 3, 4)
lista = MinhaLista([1, 4, 6, 8, 9])
lista.append(10)
