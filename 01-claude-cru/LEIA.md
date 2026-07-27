# Estação 1 — Claude Code "cru" (sem framework)

Aqui o agente, sem nenhum framework, cria um **site de tarefas** que roda no navegador
(`localhost`), aprende uma tarefa sua (Skill) e diagnostica um bug.

> **Legenda:** ⌨️ = rode no terminal / cole no Claude · 👀 = o que aparece na tela · 💬 = o que está acontecendo.
> Use **Ctrl+C** para parar o site. Um terminal é suficiente.

### 🔧 Antes de começar
Abra a pasta `demo-agentes-ia` no editor, abra um terminal e:
```bash
cd 01-claude-cru/app
```

---

## 🎬 Cena A — O agente constrói o site sozinho

**A ideia:** numa pasta vazia, você pede um site de tarefas; o agente escreve tudo e você abre no `localhost`.
**👀 O que acontece na tela:** o agente cria os arquivos e roda os testes; depois o site de tarefas aparece no navegador.
**💡 Por que importa:** de "pasta vazia" a "site rodando" em minutos, só conversando — o agente age, não completa linha.

**Passos:**
1. ⌨️ `claude`
2. ⌨️ Cole no Claude:
   ```
   Crie um gerenciador de tarefas WEB em Python usando SÓ a biblioteca padrão (http.server),
   num arquivo servidor.py que rode em http://localhost:5000. Coloque a lógica em tarefas.py
   (funções adicionar, concluir, remover, pendentes) e testes em test_tarefas.py. Rode os
   testes com "python3 -m unittest -v". Não use Flask nem nada que precise de pip.
   ```
3. ⏱️ ~1–2 min. 👀 Ele cria os arquivos e mostra os testes `OK`.
4. ⌨️ Saia do Claude para rodar o site: `/exit`
5. ⌨️ Suba o site:
   ```bash
   python3 servidor.py
   ```
   👀 Aparece `Abra no navegador: http://localhost:5000`.
6. 👀 Abra **http://localhost:5000**: a tela de tarefas aparece. Adicione uma tarefa e clique **Adicionar** — surge na hora.
   💬 *Nada de autocomplete: foi pedido, ele construiu, e está rodando no navegador.*
7. ⌨️ Ao terminar, volte ao terminal e aperte **Ctrl+C** para parar o site.

---

## 🎬 Cena B — Ensinando uma Skill ao agente

**A ideia:** uma Skill é um manual curtinho, escrito uma vez, para o agente sempre fazer algo do jeito combinado.
**👀 O que acontece na tela:** você cria um manual "como rodar os testes"; depois o agente segue esse manual sozinho.
**💡 Por que importa:** dá para padronizar o jeito do time — escreve uma vez, vale para todos.

**Passos:**
1. ⌨️ `claude`
2. ⌨️ Cole no Claude:
   ```
   Crie um arquivo .claude/skills/rodar-testes/SKILL.md com EXATAMENTE este conteúdo:

   ---
   name: rodar-testes
   description: Use sempre que for rodar os testes deste projeto de tarefas.
   ---

   # Como rodar os testes deste projeto
   - Rode SEMPRE com: python3 -m unittest -v
   - NUNCA diga que passou sem antes ver a linha final "OK".

   Depois me confirme que criou.
   ```
3. 👀 Abra `.claude/skills/rodar-testes/SKILL.md` no editor.
   💬 *Uma skill = um nome, um "quando usar" (description) e um passo a passo. Um manual que o agente lê e segue.*
4. ⌨️ Skill nova só carrega ao reabrir: `/exit`, depois `claude`.
5. ⌨️ Cole no Claude: `/rodar-testes`
6. 👀 Ele roda os testes e mostra `OK`, seguindo o manual.
   💬 *O comando não foi dado — ele achou a skill pela descrição e seguiu sozinho.*
   ⚠️ Se `/rodar-testes` não aparecer, repita o passo 4, ou cole `Rode os testes seguindo a skill.`
7. ⌨️ `/exit`

---

## 🎬 Cena C — O agente acha um bug (visível no navegador)

**A ideia:** troca-se por uma versão quebrada; no site, clicar em "concluir" risca a tarefa errada.
**👀 O que acontece na tela:** o bug aparece na tela; depois o agente explica a causa e conserta.
**💡 Por que importa:** ele não chuta — diagnostica primeiro e prova o conserto.

**Passos:**
1. ⌨️ Coloque a versão com bug e suba o site:
   ```bash
   cp ../_gabarito/web-com-bug/*.py .
   python3 servidor.py
   ```
2. 👀 Em **http://localhost:5000**, clique no ✔️ da **segunda** tarefa: quem fica riscada é a **primeira** (a errada).
   💬 *Bug encontrado: risca a tarefa errada.*
3. ⌨️ Volte ao terminal, **Ctrl+C** para parar o site, e abra o Claude: `claude`
4. ⌨️ Cole no Claude:
   ```
   No meu site, clicar em "concluir" numa tarefa marca a tarefa de cima (a errada). Investiga a
   CAUSA-RAIZ antes de corrigir: me explica em UMA frase o que está errado, e só então conserta.
   ```
5. 👀 Ele acha o erro (`concluir` usa `indice - 1`), explica e corrige.
   ⌨️ `/exit` e suba de novo (`python3 servidor.py`) para mostrar consertado. **Ctrl+C** no fim.
   💬 *A causa foi encontrada antes do remendo.*

---

## 🆘 Se algo travar
Site pronto e testado em `_gabarito/web/`:
```bash
cd ../_gabarito/web && python3 servidor.py     # http://localhost:5000 funcionando
```
Versão com bug para exibir: `_gabarito/web-com-bug/` (o erro é o `indice - 1` no `tarefas.py`).
