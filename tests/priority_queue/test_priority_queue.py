from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 10})
    queue.enqueue({"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 5})
    queue.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 2})
    queue.enqueue({"nome_do_arquivo": "arquivo4.txt", "qtd_linhas": 1})
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(300)
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 2,
    }
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo4.txt",
        "qtd_linhas": 1,
    }
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 10,
    }
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 5,
    }
    queue.enqueue({"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 15})
    queue.enqueue({"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 7})
    queue.enqueue({"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 8})
    queue.enqueue({"nome_do_arquivo": "arquivo4.txt", "qtd_linhas": 9})
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 15,
    }
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 7,
    }
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 8,
    }
    assert queue.dequeue() == {
        "nome_do_arquivo": "arquivo4.txt",
        "qtd_linhas": 9,
    }
