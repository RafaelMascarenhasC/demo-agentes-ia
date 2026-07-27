"""Mini gerenciador de tarefas — base para a feature do superpowers.

Estado inicial: mesmo projeto da Estação 1, JÁ funcionando.
A feature da demo vai ADICIONAR prioridade às tarefas em cima disto.
"""


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
