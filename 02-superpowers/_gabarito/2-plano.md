# Plano — Prioridade nas tarefas (exemplo do que a fase `writing-plans` gera)

## Tarefa 1 — Campo prioridade em `adicionar`
- `adicionar(tarefas, titulo, prioridade="normal")`; validar contra {alta, normal, baixa}.
- Teste: nova tarefa nasce `normal`; prioridade inválida levanta `ValueError`.

## Tarefa 2 — `pendentes_ordenadas`
- Nova função que filtra pendentes e ordena por peso (alta<normal<baixa), estável.
- Teste: ordem correta; empate preserva inserção; tarefas feitas ficam de fora.

## Tarefa 3 — Regressão
- Rodar toda a suíte; garantir que `pendentes`, `concluir`, `remover` seguem passando.

Dependências: Tarefa 2 depende da 1. Tarefa 3 fecha.
