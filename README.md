# 🤖 demo-agentes-ia

Projetos de demonstração para a palestra **"Agentes de IA no Desenvolvimento de Software"**
(Claude Code, superpowers e ai-jail). São 3 mini-projetos,
três formas de trabalhar com agentes de IA — do mais "cru" ao mais "preso".

| # | Pasta | Framework / modo | O que demonstra |
|---|-------|------------------|-----------------|
| 1 | [`01-claude-cru`](01-claude-cru) | Claude Code sem framework | o agente cria um **site de tarefas** (roda em localhost) do zero, cria uma Skill e acha um bug |
| 2 | [`02-superpowers`](02-superpowers) | superpowers (pipeline) | adiciona um recurso ao site (prioridade) pelo pipeline: design → plano → review |
| 3 | [`03-ai-jail`](03-ai-jail) | ai-jail (sandbox) | o mesmo site roda **preso** numa cerca: sem ver o segredo, sem rede |

> 🌐 **Os projetos das estações 1 a 3 sobem um site em `http://localhost:5000`** (Python puro, sem
> instalar nada). Roda localmente na sua máquina e é possível acessar pelo navegador.

Cada pasta tem um **`LEIA.md`** com os comandos e prompts exatos, e um **`_gabarito/`** com o
resultado pronto, que serve de referência e fallback.

---

## 📊 Slides da apresentação
- 📄 **[Ver os slides (PDF)](apresentacao/Apresentacao_Agentes_IA_ClaudeCode.pdf)** — clique e o
  GitHub abre o visualizador direto no navegador (9 slides).
- 📥 **[Baixar em PowerPoint (.pptx)](apresentacao/Apresentacao_Agentes_IA_ClaudeCode.pptx)** — para editar/apresentar.

---

## 📑 Índice
- [Slides da apresentação](#-slides-da-apresentação)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação-todas-as-formas)
- [Acessar e usar no navegador](#-acessar-e-usar-no-navegador)
- [Como usar cada estação](#-como-usar-cada-estação)
- [Segurança e o arquivo .env](#-segurança-e-o-arquivo-env)
- [Créditos e links](#-créditos-e-links)

---

## ✅ Pré-requisitos

| Ferramenta | Para quê | Obrigatório? |
|------------|----------|--------------|
| **Git** | clonar o repositório | sim |
| **Python 3.9+** | rodar os projetos e testes | sim |
| **Claude Code** | o agente de IA (todas as estações) | sim |
| **superpowers** (plugin) | estação 2 | só p/ a estação 2 |
| **ai-jail** + **bubblewrap** | estação 3 (sandbox) | só p/ a estação 3 (Linux/macOS) |

---

## 📦 Instalação (todas as formas)

### 1. Obter este repositório

**Clonar com SSH:**
```bash
git clone git@github.com:RafaelMascarenhasC/demo-agentes-ia.git
cd demo-agentes-ia
```

**Clonar com HTTPS:**
```bash
git clone https://github.com/RafaelMascarenhasC/demo-agentes-ia.git
cd demo-agentes-ia
```

**Com o GitHub CLI:**
```bash
gh repo clone RafaelMascarenhasC/demo-agentes-ia
cd demo-agentes-ia
```

**Sem git (baixar ZIP):** botão verde **`< > Code`** no GitHub → **Download ZIP** → extrair.

### 2. Python
Já vem no macOS/Linux. Confirme:
```bash
python3 --version    # precisa ser 3.9 ou maior
```
Os testes usam só a biblioteca padrão (`unittest`) — não precisa instalar nada.

### 3. Claude Code
Instale conforme a [documentação oficial](https://docs.claude.com/en/docs/claude-code). Em geral:
```bash
curl -fsSL https://claude.ai/install.sh | bash    # macOS/Linux
```
Confirme com `claude --version`. Rode `claude` dentro de uma pasta para abrir o agente.

### 4. superpowers (só para a estação 2)
É um plugin do Claude Code (público, de Jesse Vincent / `obra`). Dentro do `claude`:
```
/plugin install superpowers@claude-plugins-official
```
Confirme com `/plugin`. As skills **disparam sozinhas** quando você descreve o que quer construir
(o agente entra em brainstorming/design antes de codar). Se quiser forçar uma fase, dá pra invocá-las
como `/superpowers:brainstorming`, `/superpowers:writing-plans`, etc.

### 5. ai-jail (só para a estação 3)
Precisa do **bubblewrap** (`bwrap`) no Linux.

**Linux — dependência:**
```bash
sudo apt install bubblewrap      # Debian/Ubuntu
sudo dnf install bubblewrap      # Fedora
sudo pacman -S bubblewrap        # Arch
```

**Linux — binário pronto (sem sudo, sem brew):**
```bash
curl -fsSL https://github.com/akitaonrails/ai-jail/releases/latest/download/ai-jail-linux-x86_64.tar.gz | tar xz
mv ai-jail ~/.local/bin/         # garanta que ~/.local/bin está no PATH
ai-jail --version
```

**macOS / Linux com Homebrew:**
```bash
brew install akitaonrails/tap/ai-jail
```

**Via Cargo (Rust) ou Nix:**
```bash
cargo install ai-jail
# ou
nix run github:akitaonrails/ai-jail
```
Outras formas: <https://github.com/akitaonrails/ai-jail>

---

## 🌐 Acessar e usar no navegador

Não precisa clonar pra máquina — dá pra ver e até **rodar tudo pelo navegador**:

### Ver o código (sem instalar nada)
Abra <https://github.com/RafaelMascarenhasC/demo-agentes-ia> e navegue pelas pastas.

### Editor web (github.dev) — leitura/edição rápida
Na página do repositório, aperte a tecla **`.`** (ponto) **ou** troque `github.com` por
`github.dev` na URL:
```
https://github.dev/RafaelMascarenhasC/demo-agentes-ia
```
Abre um **VS Code no navegador** para ler e editar os arquivos (não executa código).

### Rodar de verdade no navegador (GitHub Codespaces)
Botão verde **`< > Code`** → aba **Codespaces** → **Create codespace on main**.
Sobe um VS Code completo no navegador, com terminal, onde você pode:
```bash
python3 -m unittest -v            # rodar os testes
```
E instalar o Claude Code (passo 3 acima) para reproduzir as demos. *Obs.: o Codespaces tem
cota gratuita mensal e depois é cobrado; a estação 3 (ai-jail) pode exigir permissões extras
de sandbox no ambiente do Codespaces.*

---

## 🕹️ Como usar cada estação

Cada pasta tem um `LEIA.md` com o passo a passo completo e os prompts prontos.

### Estação 1 — Claude Code "cru" → [`01-claude-cru/LEIA.md`](01-claude-cru/LEIA.md)
```bash
cd 01-claude-cru/app && claude
```
O agente cria um site de tarefas do zero; depois você o roda com `python3 servidor.py` e abre em
`http://localhost:5000`. Ainda mostra como criar uma Skill e como o agente acha um bug.
Site pronto (plano B) em `01-claude-cru/_gabarito/web/`.

### Estação 2 — superpowers → [`02-superpowers/LEIA.md`](02-superpowers/LEIA.md)
```bash
cd 02-superpowers/app && python3 servidor.py    # site "antes" em http://localhost:5000
```
Depois, com `claude`, só descreva a feature de prioridade: o superpowers **entra em design sozinho**
(o agente ataca os requisitos e exige um design aprovado antes de codar). Resultado pronto em
`02-superpowers/_gabarito/web-com-prioridade/`.

### Estação 3 — ai-jail → [`03-ai-jail/LEIA.md`](03-ai-jail/LEIA.md)
```bash
cd 03-ai-jail
cp .env.example .env
python3 servidor.py                              # site normal: rodapé "API_TOKEN: carregado"
ai-jail --mask .env python3 servidor.py          # mesmo site preso: rodapé "API_TOKEN: ausente"
ai-jail --lockdown bash -c 'curl -m 5 https://example.com'   # rede bloqueada
```
O mesmo site (`http://localhost:5000`) roda dentro da cerca, mas não consegue ler o segredo do `.env`.

---

## 🔒 Segurança e o arquivo `.env`

O `03-ai-jail/.env` **não está no repositório de propósito** (está no `.gitignore`) — segredo não
se versiona. Existe um **`.env.example`** com valores **falsos**; copie com `cp .env.example .env`.
É justamente a lição da estação 3: o ai-jail impede o agente de ler esse arquivo.

---

- **superpowers** (Jesse Vincent / `obra`) — <https://github.com/obra/superpowers>
- **ai-jail** (Fabio Akita) — <https://github.com/akitaonrails/ai-jail>

Feito para uma palestra interna. Sinta-se à vontade para reusar.
