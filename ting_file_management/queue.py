# Código tirado do course dia 3.4 de Ciência da Computação

from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if not 0 <= index < len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]

    def search_by_file(self, path_file):
        if len(self._data) == 0:
            return False
        for i in range(len(self._data)):
            if self._data[i]["nome_do_arquivo"] == path_file:
                return True

        return False
