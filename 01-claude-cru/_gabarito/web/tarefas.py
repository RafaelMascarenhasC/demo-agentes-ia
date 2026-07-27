"""Funções puras do gerenciador de tarefas (a lógica, sem web)."""


def adicionar(tarefas, titulo):
    tarefas.append({"titulo": titulo, "feita": False})
    return tarefas


def concluir(tarefas, indice):
    tarefas[indice]["feita"] = True
    return tarefas


def remover(tarefas, indice):
    del tarefas[indice]
    return tarefas


def pendentes(tarefas):
    return [t for t in tarefas if not t["feita"]]
