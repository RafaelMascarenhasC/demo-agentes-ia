"""Funções do gerenciador de tarefas — VERSAO COM BUG (para a demo de debugging).

BUG: `concluir` usa `indice - 1` em vez de `indice`. No site, ao clicar no ✔️ de uma
tarefa, quem fica riscada é a de CIMA (a errada). Deixe o Claude achar a causa-raiz.
"""


def adicionar(tarefas, titulo):
    tarefas.append({"titulo": titulo, "feita": False})
    return tarefas


def concluir(tarefas, indice):
    tarefas[indice - 1]["feita"] = True   # <-- BUG proposital
    return tarefas


def remover(tarefas, indice):
    del tarefas[indice]
    return tarefas


def pendentes(tarefas):
    return [t for t in tarefas if not t["feita"]]
