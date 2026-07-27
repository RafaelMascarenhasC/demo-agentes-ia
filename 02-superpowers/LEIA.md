# Estação 2 — superpowers (o mesmo agente, com processo)

Aqui o agente "cru" vira um **processo de engenharia**, com etapas que forçam pensar antes de codar.
A tarefa é adicionar um recurso ao site — mas do jeito certo.

> **Legenda:** ⌨️ = rode no terminal / cole no Claude · 👀 = o que aparece na tela · 💬 = o que está acontecendo.
> Use **Ctrl+C** para parar o site.

### 🔧 Antes de começar — o site "antes"
```bash
cd 02-superpowers/app
python3 servidor.py
```
👀 Abra **http://localhost:5000**: o site de tarefas, ainda sem prioridade.
⌨️ Aperte **Ctrl+C** para parar antes de seguir.

---

## 🎬 Cena principal — Ele se recusa a codar sem um plano

**A ideia:** você pede a feature de prioridade; em vez de já codar, o agente interroga o pedido e exige um design aprovado.
**👀 O que acontece na tela:** o agente faz perguntas espertas (padrão? empate? valor inválido?) e não escreve código antes da aprovação.
**💡 Por que importa:** é o agente com engenharia em volta — pensa nos casos de borda antes e deixa rastro de cada fase.

**Passos:**
1. ⌨️ `claude`
2. ⌨️ Cole no Claude (sem nenhum comando — o superpowers entra em design sozinho):
   ```
   Quero adicionar prioridade (alta/normal/baixa) às tarefas do site: escolher ao adicionar,
   mostrar uma etiqueta colorida e ordenar as pendentes por prioridade. O código está em
   servidor.py e tarefas.py. Veja também o app/FEATURE.md.
   ```
3. 👀 Ele entra na fase de design e começa a fazer perguntas.
   💬 *Nenhuma linha de código ainda: primeiro ele ataca o pedido, que estava cheio de buracos.*
4. ⌨️ Responda as perguntas. Sugestão, se precisar:
   *"Padrão normal; empate mantém a ordem de entrada; só pendentes entram na ordenação; prioridade inválida dá erro."*
5. 👀 Ele monta um documento de design e pede aprovação.
   💬 *Só com o design aprovado ele poderia codar — esse é o gate.*

---

## 🎬 Cena extra — Deixar implementar e ver no site (opcional)

**Passos:**
1. ⌨️ Diga ao Claude: **"pode gerar o plano e implementar"** → ele segue pro plano e começa a implementar + testar.
2. Ao terminar: ⌨️ `/exit` e suba o site:
   ```bash
   python3 servidor.py
   ```
   👀 No navegador, as tarefas agora têm **etiqueta de prioridade** e vêm **ordenadas**.
   💬 *Mesma feature do "cru", mas com design, plano, implementação e review — cada fase com uma checagem.*
   ⌨️ **Ctrl+C** no fim.

---

## 🆘 Se o fluxo travar ou faltar tempo
Resultado pronto rodando no navegador:
```bash
cd ../_gabarito/web-com-prioridade && python3 servidor.py     # http://localhost:5000 com prioridade
```
E veja o que cada fase gera: `_gabarito/1-design.md`, `2-plano.md`, `3-review.md` (veredicto **Approved**).
