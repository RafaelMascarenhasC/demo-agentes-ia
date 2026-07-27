# Estação 3 — ai-jail (o cadeado / a cerca de segurança)

Aqui o mesmo site roda **dentro de uma cerca**: o agente/app não consegue ler o segredo (`.env`)
nem acessar a internet. Essencial ao lidar com dados sensíveis.

> **Legenda:** ⌨️ = rode no terminal · 👀 = o que aparece na tela · 💬 = o que está acontecendo.
> Use **Ctrl+C** para parar o site.

### 🔧 Antes de começar
```bash
cd 03-ai-jail
cp .env.example .env      # cria um .env local com um segredo FALSO (não vai para o git)
```

---

## 🎬 Abertura — o site normal LÊ o segredo

**A ideia:** rodando normalmente, o app enxerga o segredo do `.env`.

1. ⌨️ `python3 servidor.py`
2. 👀 Abra **http://localhost:5000**: no rodapé, **"🔑 API_TOKEN: carregado"**.
   💬 *O app leu o segredo numa boa. Normalmente o agente também leria.*
3. ⌨️ **Ctrl+C** para parar.

---

## 🎬 Cena A — A cerca desenhada (`--dry-run`)

**A ideia:** dá para ver a cerca antes de rodar qualquer coisa.

⌨️ `ai-jail --dry-run --mask .env python3 servidor.py`
👀 Imprime a configuração da cerca (linhas `bwrap ...`) e não executa nada.

---

## 🎬 Cena B — O mesmo site, mas o segredo some (`--mask`) ⭐

**A ideia:** o mesmo site roda dentro da cerca; funciona, mas não enxerga o segredo.
**👀 O que acontece na tela:** o site igualzinho no navegador, mas o rodapé agora diz **"🔒 API_TOKEN: ausente"**.
**💡 Por que importa:** o `.env` está lá, mas a cerca entrega vazio para quem roda dentro dela.

1. ⌨️ `ai-jail --mask .env python3 servidor.py`
2. 👀 Abra **http://localhost:5000**: rodapé **"🔒 API_TOKEN: ausente"**.
   💬 *Mesmo site, mesma pasta — mas dentro da cerca o segredo sumiu.*
3. ⌨️ **Ctrl+C** para parar.

---

## 🎬 Cena C — A internet cai (`--lockdown`)

**A ideia:** no modo mais estrito, nem à internet o processo chega.

⌨️ `ai-jail --lockdown bash -c 'curl -m 5 https://example.com'`
👀 Falha: `Could not resolve host: example.com`.
💬 *Em lockdown não há acesso à rede. Não é 100%, mas é o suficiente — backup continua essencial.*

---

## 🆘 Se algo demorar
Versão instantânea da Cena B, sem navegador:
```bash
ai-jail --mask .env bash -c 'echo "o que a cerca deixa ver do .env:"; cat .env'
```
👀 Sai **vazio** — o segredo foi escondido.
