import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            print(f"Formato inválido", file=sys.stderr)
        with open(path_file, "r") as file:
            return file.read().split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


if __name__ == "__main__":
    print(txt_importer("statics/arquivo_teste.txt"))
    print(txt_importer("statics/arquivo_teste.csv"))
    print(txt_importer("statics/arquivo_nao_existe.txt"))
