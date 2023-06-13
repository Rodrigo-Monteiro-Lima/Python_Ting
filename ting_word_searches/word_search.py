from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    arr = []
    for i in range(len(instance)):
        current = instance.search(i)
        dict = {
            "palavra": word,
            "arquivo": current["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for phrase in current["linhas_do_arquivo"]:
            if word.lower() in phrase.lower():
                dict["ocorrencias"].append(
                    {"linha": current["linhas_do_arquivo"].index(phrase) + 1}
                )
        if dict["ocorrencias"]:
            arr.append(dict)
    return arr


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


if __name__ == "__main__":
    project = Queue()
    process("statics/nome_pedro.txt", project)
    exists_word("pedroasdasd", project)
