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
                    {
                        "linha": current["linhas_do_arquivo"].index(phrase)
                        + 1,
                        "conteudo": phrase,
                    }
                )
        if dict["ocorrencias"]:
            arr.append(dict)
    return arr
