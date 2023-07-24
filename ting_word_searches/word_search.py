def exists_word(word, instance, phrases=False):
    occurrences_list = []
    for i in range(len(instance)):
        current = instance.search(i)
        result_dict = {
            "palavra": word,
            "arquivo": current["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for idx, phrase in enumerate(current["linhas_do_arquivo"], 1):
            if word.lower() in phrase.lower():
                if phrases:
                    result_dict["ocorrencias"].append(
                        {
                            "linha": idx,
                            "conteudo": phrase,
                        }
                    )
                else:
                    result_dict["ocorrencias"].append(
                        {
                            "linha": idx,
                        }
                    )
        if result_dict["ocorrencias"]:
            occurrences_list.append(result_dict)
    return occurrences_list


def search_by_word(word, instance):
    return exists_word(word, instance, True)
