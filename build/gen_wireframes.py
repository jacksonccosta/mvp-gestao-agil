# -*- coding: utf-8 -*-
"""Gera wireframes de BAIXA FIDELIDADE (estilo Figma) em PNG para a pasta /wireframes.

Estética: tons de cinza, blocos, linhas-marcador de texto e anotações. Representa as
telas da Sprint 1 do produto 'Minha Agenda de Tarefas'.
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "wireframes"))
os.makedirs(OUT, exist_ok=True)

# Paleta low-fi (grayscale + 1 cor de acento para anotações)
BG      = (255, 255, 255)
INK     = (33, 37, 41)
GRAY    = (108, 117, 125)
LIGHT   = (233, 236, 239)
MED     = (206, 212, 218)
DARK    = (73, 80, 87)
LINE    = (173, 181, 189)
ACCENT  = (13, 110, 253)     # azul p/ botões "primários" (contorno)
NOTE    = (214, 51, 108)     # rosa p/ anotações de UX
PLACE   = (222, 226, 230)

def font(size, bold=False):
    paths = [r"C:\Windows\Fonts\segoeui.ttf", r"C:\Windows\Fonts\arial.ttf"]
    bpaths = [r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\arialbd.ttf"]
    for p in (bpaths if bold else paths):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

F   = lambda s: font(s)
FB  = lambda s: font(s, True)

def canvas(w=1000, h=1400):
    img = Image.new("RGB", (w, h), BG)
    return img, ImageDraw.Draw(img)

def rrect(d, box, r=10, fill=None, outline=LINE, width=2):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

def text(d, xy, s, f, fill=INK, anchor="la"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)

def textlines(d, x, y, width, n=3, gap=16, color=LINE, h=7, last_ratio=0.6):
    """Linhas-marcador de texto (placeholder lorem)."""
    for i in range(n):
        w = width if i < n-1 else int(width*last_ratio)
        d.rounded_rectangle([x, y, x+w, y+h], radius=h//2, fill=color)
        y += gap
    return y

def btn(d, box, label, primary=True, f=None):
    f = f or FB(20)
    if primary:
        d.rounded_rectangle(box, radius=8, fill=ACCENT)
        cx = (box[0]+box[2])//2; cy = (box[1]+box[3])//2
        text(d, (cx, cy), label, f, fill=(255,255,255), anchor="mm")
    else:
        d.rounded_rectangle(box, radius=8, outline=ACCENT, width=2)
        cx = (box[0]+box[2])//2; cy = (box[1]+box[3])//2
        text(d, (cx, cy), label, f, fill=ACCENT, anchor="mm")

def note(d, x, y, s, anchor="la"):
    # marcador losango desenhado (evita depender de glifos da fonte)
    cy = y + 8
    d.polygon([(x+5, cy-5), (x+10, cy), (x+5, cy+5), (x, cy)], fill=NOTE)
    text(d, (x+18, y), s, F(15), fill=NOTE, anchor=anchor)

def navbar(d, w, title="Minha Agenda de Tarefas"):
    d.rectangle([0,0,w,80], fill=LIGHT)
    d.ellipse([24,18,68,62], outline=GRAY, width=2)        # logo placeholder
    text(d, (40,40), "logo", F(13), fill=GRAY, anchor="mm")
    text(d, (84,40), title, FB(28), fill=DARK, anchor="lm")

def card_section(d, box, title=None):
    rrect(d, box, r=12, fill=(252,252,253), outline=MED, width=2)
    if title:
        text(d, (box[0]+24, box[1]+22), title, FB(22), fill=INK)

def footer(d, w, h):
    d.rectangle([0,h-50,w,h], fill=LIGHT)
    text(d, (w//2, h-25), "Desenvolvido por Jackson Costa — PUC-Rio", F(14), fill=GRAY, anchor="mm")

def frame_label(d, w, name, screen_no):
    text(d, (24, 100), f"Wireframe {screen_no} — {name}", FB(18), fill=GRAY)
    d.line([24,128,w-24,128], fill=LIGHT, width=2)


# ---------------------------------------------------------------------------
# 1) Seleção / Cadastro de usuário
# ---------------------------------------------------------------------------
def wf_usuarios():
    w, h = 1000, 760
    img, d = canvas(w, h)
    navbar(d, w)
    frame_label(d, w, "Selecao e cadastro de usuario (US01, US02)", 1)

    box = [40, 150, w-40, 470]
    card_section(d, box)
    # Coluna esquerda: selecionar
    text(d, (64, 180), "Selecionar Usuário", FB(22))
    text(d, (64, 220), "Escolha um usuário para ver as tarefas:", F(16), fill=GRAY)
    rrect(d, [64, 250, 470, 296], r=8, fill=BG, outline=LINE, width=2)
    text(d, (84, 273), "Selecione um usuário...", F(16), fill=GRAY, anchor="lm")
    d.polygon([(440,268),(456,268),(448,280)], fill=GRAY)     # seta dropdown
    note(d, 64, 320, "Dropdown lista todos os usuários cadastrados")

    # Divisor
    d.line([520,180,520,440], fill=LIGHT, width=2)

    # Coluna direita: cadastrar
    text(d, (560, 180), "Cadastrar Novo Usuário", FB(22))
    text(d, (560, 222), "Nome", F(15), fill=GRAY)
    rrect(d, [560, 244, w-64, 286], r=8, fill=BG, outline=LINE, width=2)
    text(d, (560, 300), "Email", F(15), fill=GRAY)
    rrect(d, [560, 322, w-64, 364], r=8, fill=BG, outline=LINE, width=2)
    btn(d, [560, 386, 760, 430], "Cadastrar Usuário", primary=False)
    note(d, 64, 410, "Validação: e-mail único e formato válido (US01)")

    # Estado vazio
    box2 = [40, 500, w-40, 690]
    card_section(d, box2)
    text(d, (w//2, 560), "Selecione um usuário para visualizar o quadro de tarefas", F(18), fill=GRAY, anchor="mm")
    rrect(d, [w//2-120, 600, w//2+120, 650], r=8, fill=LIGHT, outline=MED, width=2)
    text(d, (w//2, 625), "( quadro aparece aqui )", F(14), fill=GRAY, anchor="mm")

    footer(d, w, h)
    img.save(os.path.join(OUT, "01-selecao-cadastro-usuario.png"))


# ---------------------------------------------------------------------------
# 2) Nova tarefa (formulário) + sugerir
# ---------------------------------------------------------------------------
def wf_nova_tarefa():
    w, h = 1000, 760
    img, d = canvas(w, h)
    navbar(d, w)
    frame_label(d, w, "Criacao de tarefa + sugestao (US03, US08)", 2)

    # Usuário ativo
    rrect(d, [40, 150, w-40, 210], r=10, fill=LIGHT, outline=MED, width=2)
    text(d, (64, 180), "Usuário ativo:", F(16), fill=GRAY, anchor="lm")
    text(d, (200, 180), "Carla (designer freelancer)", FB(18), anchor="lm")

    box = [40, 230, w-40, 620]
    card_section(d, box)
    text(d, (64, 256), "Nova Tarefa", FB(24))
    btn(d, [760, 250, w-64, 296], "Sugerir Tarefa", primary=False, f=FB(16))
    note(d, 64, 300, "Botão chama API externa de sugestões (US08)")

    text(d, (64, 340), "Título", F(16), fill=GRAY)
    rrect(d, [64, 364, w-64, 410], r=8, fill=BG, outline=LINE, width=2)
    text(d, (84, 387), "Ex: Fazer compras", F(15), fill=MED, anchor="lm")

    text(d, (64, 430), "Descrição", F(16), fill=GRAY)
    rrect(d, [64, 454, w-64, 560], r=8, fill=BG, outline=LINE, width=2)
    textlines(d, 84, 478, 700, n=3, gap=20, color=PLACE)

    btn(d, [64, 576, 280, 604], "Adicionar Tarefa", primary=True, f=FB(16))
    note(d, 64, 640, "Título obrigatório; descrição opcional. Tarefa entra em 'A Fazer'.")

    footer(d, w, h)
    img.save(os.path.join(OUT, "02-nova-tarefa.png"))


# ---------------------------------------------------------------------------
# 3) Quadro Kanban (3 colunas)
# ---------------------------------------------------------------------------
def kanban_card(d, x, y, w, title, lines=2, with_actions=True):
    bh = 110
    rrect(d, [x, y, x+w, y+bh], r=10, fill=BG, outline=MED, width=2)
    text(d, (x+16, y+18), title, FB(16))
    textlines(d, x+16, y+46, w-60, n=lines, gap=14, color=PLACE, h=6)
    if with_actions:
        # mini-botões de ação
        rrect(d, [x+w-100, y+bh-34, x+w-58, y+bh-12], r=5, outline=LINE, width=2)
        rrect(d, [x+w-50, y+bh-34, x+w-12, y+bh-12], r=5, outline=NOTE, width=2)
    return y + bh + 16

def column(d, x, top, w, title, color, cards):
    # header
    rrect(d, [x, top, x+w, top+44], r=8, fill=color)
    text(d, (x+w//2, top+22), title, FB(18), fill=(255,255,255), anchor="mm")
    y = top + 60
    for c in cards:
        y = kanban_card(d, x, y, w, c["t"], c.get("l",2))
    return y

def wf_kanban():
    w, h = 1100, 820
    img, d = canvas(w, h)
    navbar(d, w)
    frame_label(d, w, "Quadro Kanban + filtros (US04, US05, US06, US07)", 3)

    # filtros
    text(d, (40, 158), "Filtrar:", FB(16), anchor="lm")
    fx = 120
    for label, on in [("Todos", True), ("A Fazer", False), ("Em Andamento", False), ("Concluído", False)]:
        tw = d.textlength(label, font=F(15)) + 32
        rrect(d, [fx, 142, fx+tw, 176], r=16, fill=(ACCENT if on else BG),
              outline=ACCENT, width=2)
        text(d, (fx+tw/2, 159), label, F(15), fill=((255,255,255) if on else ACCENT), anchor="mm")
        fx += tw + 12
    note(d, 40, 188, "Filtro por status (US07)")

    top = 220
    colw = (w - 80 - 2*24) // 3
    x = 40
    column(d, x, top, colw, "A Fazer", (108,117,125),
           [{"t":"Revisar briefing","l":2},{"t":"Comprar materiais","l":1},{"t":"Responder e-mails","l":2}])
    x += colw + 24
    column(d, x, top, colw, "Em Andamento", (255,193,7),
           [{"t":"Design da landing","l":2},{"t":"Protótipo no Figma","l":2}])
    x += colw + 24
    column(d, x, top, colw, "Concluído", (25,135,84),
           [{"t":"Reunião com cliente","l":1},{"t":"Enviar proposta","l":1}])

    # legenda de ações
    ly = top + 520
    rrect(d, [40, ly, 80, ly+26], r=5, outline=LINE, width=2)
    text(d, (92, ly+13), "Mudar status (US05)", F(15), fill=GRAY, anchor="lm")
    rrect(d, [320, ly, 360, ly+26], r=5, outline=NOTE, width=2)
    text(d, (372, ly+13), "Excluir (abre modal de confirmação — US06)", F(15), fill=GRAY, anchor="lm")

    footer(d, w, h)
    img.save(os.path.join(OUT, "03-quadro-kanban.png"))


# ---------------------------------------------------------------------------
# 4) Modal de confirmação de exclusão
# ---------------------------------------------------------------------------
def wf_modal():
    w, h = 1000, 720
    img, d = canvas(w, h)
    navbar(d, w)
    frame_label(d, w, "Modal de confirmacao de exclusao (US06)", 4)

    # fundo esmaecido
    d.rectangle([0, 140, w, h-50], fill=(245,246,247))
    text(d, (w//2, 200), "( quadro de tarefas ao fundo, esmaecido )", F(16), fill=MED, anchor="mm")

    # modal
    mw, mh = 520, 280
    mx, my = (w-mw)//2, 280
    d.rounded_rectangle([mx, my, mx+mw, my+mh], radius=14, fill=BG, outline=MED, width=2)
    # header
    text(d, (mx+28, my+30), "Confirmar Exclusão", FB(22))
    # botão fechar (X desenhado)
    cxp, cyp = mx+mw-34, my+34
    d.line([cxp, cyp, cxp+14, cyp+14], fill=GRAY, width=2)
    d.line([cxp+14, cyp, cxp, cyp+14], fill=GRAY, width=2)
    d.line([mx, my+70, mx+mw, my+70], fill=LIGHT, width=2)
    # body
    text(d, (mx+28, my+110), "Tem certeza que deseja excluir esta tarefa?", F(18))
    # footer buttons
    btn(d, [mx+mw-330, my+mh-64, mx+mw-180, my+mh-22], "Cancelar", primary=False, f=FB(16))
    d.rounded_rectangle([mx+mw-160, my+mh-64, mx+mw-28, my+mh-22], radius=8, fill=NOTE)
    text(d, (mx+mw-94, my+mh-43), "Excluir", FB(16), fill=(255,255,255), anchor="mm")

    note(d, mx, my+mh+24, "Ação destrutiva exige confirmação explícita (boa prática de UX)")

    footer(d, w, h)
    img.save(os.path.join(OUT, "04-modal-exclusao.png"))


# ---------------------------------------------------------------------------
# 5) Versão mobile (responsivo)
# ---------------------------------------------------------------------------
def wf_mobile():
    w, h = 480, 920
    img, d = canvas(w, h)
    # moldura do celular
    d.rounded_rectangle([10,10,w-10,h-10], radius=28, outline=MED, width=3)
    inner = 26
    # navbar
    d.rectangle([inner,40,w-inner,100], fill=LIGHT)
    text(d, ((w)//2, 70), "Minha Agenda de Tarefas", FB(18), fill=DARK, anchor="mm")
    text(d, (inner+10, 130), "Wireframe 5 — Mobile (RNF responsividade)", FB(13), fill=GRAY)

    # seletor
    rrect(d, [inner, 160, w-inner, 200], r=8, fill=BG, outline=LINE, width=2)
    text(d, (inner+14, 180), "Carla", F(15), fill=GRAY, anchor="lm")
    d.polygon([(w-inner-28,176),(w-inner-14,176),(w-inner-21,186)], fill=GRAY)

    # nova tarefa colapsada
    btn(d, [inner, 214, w-inner, 252], "+ Nova Tarefa", primary=True, f=FB(15))

    # filtros (scroll horizontal)
    fx = inner
    for label, on in [("Todos", True), ("A Fazer", False), ("Em And.", False)]:
        tw = d.textlength(label, font=F(13)) + 24
        rrect(d, [fx, 268, fx+tw, 298], r=14, fill=(ACCENT if on else BG), outline=ACCENT, width=2)
        text(d, (fx+tw/2, 283), label, F(13), fill=((255,255,255) if on else ACCENT), anchor="mm")
        fx += tw + 8

    # colunas empilhadas
    y = 320
    for title, color, cards in [
        ("A Fazer", (108,117,125), ["Revisar briefing","Comprar materiais"]),
        ("Em Andamento", (255,193,7), ["Design da landing"]),
        ("Concluído", (25,135,84), ["Enviar proposta"]),
    ]:
        rrect(d, [inner, y, w-inner, y+34], r=8, fill=color)
        text(d, (w//2, y+17), title, FB(15), fill=(255,255,255), anchor="mm")
        y += 44
        for c in cards:
            rrect(d, [inner, y, w-inner, y+72], r=8, fill=BG, outline=MED, width=2)
            text(d, (inner+12, y+14), c, FB(14))
            textlines(d, inner+12, y+38, w-2*inner-60, n=2, gap=12, color=PLACE, h=5)
            y += 84
        y += 8

    text(d, (w//2, h-30), "Colunas empilham em telas pequenas", F(12), fill=GRAY, anchor="mm")
    img.save(os.path.join(OUT, "05-mobile-responsivo.png"))


if __name__ == "__main__":
    wf_usuarios()
    wf_nova_tarefa()
    wf_kanban()
    wf_modal()
    wf_mobile()
    print("Wireframes gerados em:", OUT)
    for f in sorted(os.listdir(OUT)):
        print(" -", f)
