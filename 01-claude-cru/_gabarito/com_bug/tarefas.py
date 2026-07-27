"""Mini gerenciador de tarefas — VERSAO COM BUG (para a demo de debugging).

O bug esta em `concluir`: usa `indice - 1` em vez de `indice`, entao marca
a tarefa ERRADA. O teste `test_concluir_marca_a_tarefa_certa` vai falhar.
Deixe o Claude descobrir a causa-raiz sozinho — nao entregue a resposta.
"""


def adicionar(tarefas, titulo):
    tarefas.append({"titulo": titulo, "feita": False})
    return tarefas


def concluir(tarefas, indice):
    tarefas[indice - 1]["feita"] = True
    return tarefas


def remover(tarefas, indice):
    del tarefas[indice]
    return tarefas


def pendentes(tarefas):
    return [t for t in tarefas if not t["feita"]]
