"""Mini gerenciador de tarefas — projeto de demonstração (versão correta)."""


def adicionar(tarefas, titulo):
    """Adiciona uma tarefa nova (pendente) à lista."""
    tarefas.append({"titulo": titulo, "feita": False})
    return tarefas


def concluir(tarefas, indice):
    """Marca a tarefa da posição `indice` como feita."""
    tarefas[indice]["feita"] = True
    return tarefas


def remover(tarefas, indice):
    """Remove a tarefa da posição `indice`."""
    del tarefas[indice]
    return tarefas


def pendentes(tarefas):
    """Retorna só as tarefas que ainda não foram feitas."""
    return [t for t in tarefas if not t["feita"]]
