"""Gerenciador de tarefas WEB — roda em http://localhost:5000

Usa só a biblioteca padrão do Python (http.server), então roda com:
    python3 servidor.py
Sem pip, sem internet. Para parar: Ctrl+C.
"""
import os
import html
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from tarefas import adicionar, concluir, remover, pendentes

PORTA = 5000

# "banco de dados" em memória (some ao reiniciar) — suficiente para a demo
TAREFAS = []
adicionar(TAREFAS, "Preparar a palestra")
adicionar(TAREFAS, "Testar a demo no localhost")


def carregar_env():
    """Lê um .env simples (KEY=VALUE) da pasta atual, se existir."""
    if os.path.exists(".env"):
        for linha in open(".env", encoding="utf-8"):
            linha = linha.strip()
            if linha and not linha.startswith("#") and "=" in linha:
                chave, valor = linha.split("=", 1)
                os.environ.setdefault(chave.strip(), valor.strip())


PAGINA = """<!doctype html>
<html lang="pt-br"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minhas Tarefas</title>
<style>
  body {{ font-family: system-ui, sans-serif; background:#0f172a; color:#e2e8f0;
         display:flex; justify-content:center; padding:40px 16px; }}
  .card {{ background:#1e293b; width:100%; max-width:520px; border-radius:16px;
           padding:28px 32px; box-shadow:0 10px 40px rgba(0,0,0,.4); }}
  h1 {{ margin:0 0 4px; font-size:28px; }}
  .sub {{ color:#94a3b8; margin:0 0 20px; font-size:14px; }}
  form {{ display:flex; gap:8px; margin-bottom:18px; }}
  input {{ flex:1; padding:12px 14px; border-radius:10px; border:1px solid #334155;
           background:#0f172a; color:#e2e8f0; font-size:16px; }}
  button {{ padding:12px 18px; border:0; border-radius:10px; background:#6366f1;
            color:#fff; font-size:16px; cursor:pointer; }}
  ul {{ list-style:none; padding:0; margin:0; }}
  li {{ display:flex; justify-content:space-between; align-items:center;
        padding:12px 4px; border-bottom:1px solid #334155; font-size:17px; }}
  li a {{ text-decoration:none; font-size:18px; margin-left:10px; }}
  .feita {{ text-decoration:line-through; opacity:.45; }}
  .badge {{ margin-top:22px; font-size:13px; color:#94a3b8; }}
  .foot {{ margin-top:6px; font-size:12px; color:#475569; }}
</style></head>
<body><div class="card">
  <h1>📋 Minhas Tarefas</h1>
  <p class="sub">{n} pendente(s)</p>
  <form action="/add" method="get">
    <input name="titulo" placeholder="Nova tarefa..." autofocus required>
    <button>Adicionar</button>
  </form>
  <ul>{itens}</ul>
  <div class="badge">{badge}</div>
  <div class="foot">Servido por Python puro (http.server) em http://localhost:{porta}</div>
</div></body></html>"""


def render():
    token = os.environ.get("API_TOKEN")
    if token:
        badge = "🔑 API_TOKEN: <b>carregado</b> (o app leu o segredo do .env)"
    else:
        badge = "🔒 API_TOKEN: <b>ausente</b> — o segredo não chegou ao app (sandbox?)"
    itens = []
    for i, t in enumerate(TAREFAS):
        classe = "feita" if t["feita"] else ""
        titulo = html.escape(t["titulo"])
        itens.append(
            f'<li><span class="{classe}">{titulo}</span>'
            f'<span><a href="/concluir?i={i}" title="concluir">✔️</a>'
            f'<a href="/remover?i={i}" title="remover">🗑️</a></span></li>'
        )
    corpo = "".join(itens) or '<li style="color:#64748b">Nenhuma tarefa ainda.</li>'
    return PAGINA.format(itens=corpo, n=len(pendentes(TAREFAS)), badge=badge, porta=PORTA)


class Handler(BaseHTTPRequestHandler):
    def _redirect(self):
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

    def _html(self, texto):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(texto.encode("utf-8"))

    def do_GET(self):
        url = urlparse(self.path)
        params = parse_qs(url.query)
        if url.path == "/":
            self._html(render())
        elif url.path == "/add":
            titulo = (params.get("titulo") or [""])[0].strip()
            if titulo:
                adicionar(TAREFAS, titulo)
            self._redirect()
        elif url.path == "/concluir":
            i = int((params.get("i") or ["-1"])[0])
            if 0 <= i < len(TAREFAS):
                concluir(TAREFAS, i)
            self._redirect()
        elif url.path == "/remover":
            i = int((params.get("i") or ["-1"])[0])
            if 0 <= i < len(TAREFAS):
                remover(TAREFAS, i)
            self._redirect()
        else:
            self.send_error(404)

    def log_message(self, *args):
        pass  # silencia o log a cada request, pra tela ficar limpa na demo


if __name__ == "__main__":
    carregar_env()
    print(f"➡️  Abra no navegador: http://localhost:{PORTA}  (Ctrl+C para parar)")
    HTTPServer(("127.0.0.1", PORTA), Handler).serve_forever()
