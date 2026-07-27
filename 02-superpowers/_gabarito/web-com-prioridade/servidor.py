"""Gerenciador de tarefas WEB COM PRIORIDADE — http://localhost:5000 (só biblioteca padrão).

Roda com: python3 servidor.py   (Ctrl+C para parar)
"""
import os
import html
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from tarefas import adicionar, concluir, remover, pendentes, NIVEIS

PORTA = 5000

TAREFAS = []
adicionar(TAREFAS, "Preparar a palestra", "alta")
adicionar(TAREFAS, "Testar a demo no localhost", "normal")
adicionar(TAREFAS, "Comprar café", "baixa")

CORES = {"alta": "#ef4444", "normal": "#6366f1", "baixa": "#64748b"}

PAGINA = """<!doctype html>
<html lang="pt-br"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minhas Tarefas</title>
<style>
  body {{ font-family: system-ui, sans-serif; background:#0f172a; color:#e2e8f0;
         display:flex; justify-content:center; padding:40px 16px; }}
  .card {{ background:#1e293b; width:100%; max-width:560px; border-radius:16px;
           padding:28px 32px; box-shadow:0 10px 40px rgba(0,0,0,.4); }}
  h1 {{ margin:0 0 4px; font-size:28px; }}
  .sub {{ color:#94a3b8; margin:0 0 20px; font-size:14px; }}
  form {{ display:flex; gap:8px; margin-bottom:18px; }}
  input, select {{ padding:12px 14px; border-radius:10px; border:1px solid #334155;
           background:#0f172a; color:#e2e8f0; font-size:16px; }}
  input {{ flex:1; }}
  button {{ padding:12px 18px; border:0; border-radius:10px; background:#6366f1;
            color:#fff; font-size:16px; cursor:pointer; }}
  ul {{ list-style:none; padding:0; margin:0; }}
  li {{ display:flex; justify-content:space-between; align-items:center;
        padding:12px 4px; border-bottom:1px solid #334155; font-size:17px; }}
  li a {{ text-decoration:none; font-size:18px; margin-left:10px; }}
  .feita {{ text-decoration:line-through; opacity:.45; }}
  .tag {{ font-size:11px; font-weight:700; text-transform:uppercase; padding:3px 8px;
          border-radius:999px; color:#fff; margin-right:10px; }}
  .foot {{ margin-top:22px; font-size:12px; color:#475569; }}
</style></head>
<body><div class="card">
  <h1>📋 Minhas Tarefas</h1>
  <p class="sub">{n} pendente(s) · ordenadas por prioridade</p>
  <form action="/add" method="get">
    <input name="titulo" placeholder="Nova tarefa..." autofocus required>
    <select name="prioridade">
      <option value="alta">Alta</option>
      <option value="normal" selected>Normal</option>
      <option value="baixa">Baixa</option>
    </select>
    <button>Adicionar</button>
  </form>
  <ul>{itens}</ul>
  <div class="foot">Servido por Python puro (http.server) em http://localhost:{porta}</div>
</div></body></html>"""


def render():
    idx = list(range(len(TAREFAS)))
    pend = sorted([i for i in idx if not TAREFAS[i]["feita"]],
                  key=lambda i: NIVEIS[TAREFAS[i]["prioridade"]])
    done = [i for i in idx if TAREFAS[i]["feita"]]
    linhas = []
    for i in pend + done:
        t = TAREFAS[i]
        classe = "feita" if t["feita"] else ""
        cor = CORES[t["prioridade"]]
        tag = f'<span class="tag" style="background:{cor}">{t["prioridade"]}</span>'
        titulo = html.escape(t["titulo"])
        linhas.append(
            f'<li><span>{tag}<span class="{classe}">{titulo}</span></span>'
            f'<span><a href="/concluir?i={i}" title="concluir">✔️</a>'
            f'<a href="/remover?i={i}" title="remover">🗑️</a></span></li>'
        )
    corpo = "".join(linhas) or '<li style="color:#64748b">Nenhuma tarefa ainda.</li>'
    return PAGINA.format(itens=corpo, n=len(pendentes(TAREFAS)), porta=PORTA)


class Handler(BaseHTTPRequestHandler):
    def _redirect(self):
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

    def do_GET(self):
        url = urlparse(self.path)
        p = parse_qs(url.query)
        if url.path == "/":
            corpo = render().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(corpo)
        elif url.path == "/add":
            titulo = (p.get("titulo") or [""])[0].strip()
            prioridade = (p.get("prioridade") or ["normal"])[0]
            if titulo and prioridade in NIVEIS:
                adicionar(TAREFAS, titulo, prioridade)
            self._redirect()
        elif url.path == "/concluir":
            i = int((p.get("i") or ["-1"])[0])
            if 0 <= i < len(TAREFAS):
                concluir(TAREFAS, i)
            self._redirect()
        elif url.path == "/remover":
            i = int((p.get("i") or ["-1"])[0])
            if 0 <= i < len(TAREFAS):
                remover(TAREFAS, i)
            self._redirect()
        else:
            self.send_error(404)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"➡️  Abra no navegador: http://localhost:{PORTA}  (Ctrl+C para parar)")
    HTTPServer(("127.0.0.1", PORTA), Handler).serve_forever()
