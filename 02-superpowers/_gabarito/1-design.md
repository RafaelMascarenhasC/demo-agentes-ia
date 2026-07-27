# Design — Prioridade nas tarefas (exemplo do que a fase `brainstorming` gera)

## Requisitos (depois do ataque da fase de brainstorming)
- Níveis: `alta`, `normal`, `baixa`.
- Prioridade padrão de tarefa nova: `normal`.
- Ordenação das pendentes: alta → normal → baixa; empate mantém ordem de inserção (estável).
- Só **pendentes** entram na ordenação; tarefas feitas não aparecem.
- Prioridade inválida: levanta `ValueError` (não vira padrão silenciosamente).

## Decisões de arquitetura
- Cada tarefa ganha o campo `prioridade` (string validada contra um conjunto fixo).
- Nova função `pendentes_ordenadas(tarefas)` — não altera `pendentes` (retrocompatível).
- Ordenação via `sorted` com chave de peso {alta:0, normal:1, baixa:2}, estável por natureza.

## Fora de escopo
- Persistência, interface de linha de comando, reordenar por drag-and-drop.
