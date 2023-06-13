from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance):
    if not instance.search_by_file(path_file):
        imported_file = txt_importer(path_file)
        if isinstance(imported_file, list):
            processed_file = {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(imported_file),
                "linhas_do_arquivo": imported_file,
            }
            instance.enqueue(processed_file)
            print(processed_file, file=sys.stdout)
    return None


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")
    removed_file = instance.dequeue()
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")
    return removed_file


def file_metadata(instance, position):
    try:
        searched_file = instance.search(position)
        print(searched_file)
        return searched_file
    except IndexError:
        print("Posição inválida", file=sys.stderr)


if __name__ == "__main__":
    project = Queue()
    process("statics/novo_paradigma_globalizado-min.txt", project)
    file_metadata(project, 200)
