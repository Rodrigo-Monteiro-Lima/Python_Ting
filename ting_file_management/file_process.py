from ting_file_management.file_management import txt_importer
import sys
from ting_file_management.queue import Queue


def process(path_file, instance):
    if not instance.search_by_file(path_file):
        imported_file = txt_importer(path_file)
        if isinstance(imported_file, list):
            processed_file = {
                "nome_do_aquivo": path_file,
                "qtd_linhas": len(imported_file),
                "linhas_do_arquivo": imported_file,
            }
            instance.enqueue(processed_file)
            print(processed_file, sys.stdout)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")
    removed_file = instance.dequeue()
    return print(
        f"Arquivo {removed_file['nome_do_aquivo']} removido com sucesso"
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    a = process("statics/arquivo_teste.txt", Queue())
    print(a)
    print("'nome_do_arquivo': 'statics/arquivo_teste.txt'" in a)
