"""Funções do gerenciador de tarefas — COM PRIORIDADE (resultado da feature do superpowers)."""

NIVEIS = {"alta": 0, "normal": 1, "baixa": 2}


def adicionar(tarefas, titulo, prioridade="normal"):
    if prioridade not in NIVEIS:
        raise ValueError(f"prioridade invalida: {prioridade}")
    tarefas.append({"titulo": titulo, "feita": False, "prioridade": prioridade})
    return tarefas


def concluir(tarefas, indice):
    tarefas[indice]["feita"] = True
    return tarefas


def remover(tarefas, indice):
    del tarefas[indice]
    return tarefas


def pendentes(tarefas):
    return [t for t in tarefas if not t["feita"]]


def pendentes_ordenadas(tarefas):
    """Pendentes em ordem de prioridade (alta -> normal -> baixa), estável nos empates."""
    return sorted(pendentes(tarefas), key=lambda t: NIVEIS[t["prioridade"]])
