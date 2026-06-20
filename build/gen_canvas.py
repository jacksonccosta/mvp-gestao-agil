# -*- coding: utf-8 -*-
"""Gera a imagem do MVP Canvas (layout Caroli/Lean Inception) pronta para colar no Miro."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
os.makedirs(OUT, exist_ok=True)

W, H = 1760, 1040
BG = (255, 255, 255)
HEAD = (13, 110, 253)
HEAD2 = (10, 79, 176)
INK = (33, 37, 41)
GRAY = (90, 98, 106)
BORDER = (180, 190, 200)
TINT = (232, 241, 255)

def font(size, bold=False):
    p = r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf"
    if not os.path.exists(p):
        p = r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf"
    return ImageFont.truetype(p, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines

def panel(box, title, bullets, tint=False, title_bg=HEAD):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=12, fill=(TINT if tint else (252,252,253)), outline=BORDER, width=2)
    # header
    d.rounded_rectangle([x0, y0, x1, y0+44], radius=12, fill=title_bg)
    d.rectangle([x0, y0+30, x1, y0+44], fill=title_bg)
    tf = font(18, True)
    d.text((x0+14, y0+22), title, font=tf, fill=(255,255,255), anchor="lm")
    # bullets
    bf = font(15)
    bbf = font(15, True)
    y = y0 + 58
    maxw = x1 - x0 - 44
    for b in bullets:
        bold = b.startswith("**")
        s = b.replace("**", "")
        fnt = bbf if bold else bf
        # bullet dot
        d.ellipse([x0+16, y+6, x0+22, y+12], fill=HEAD2)
        for i, ln in enumerate(wrap(d, s, fnt, maxw)):
            d.text((x0+32, y), ln, font=fnt, fill=INK, anchor="la")
            y += 21
        y += 6

# ---- Título principal ----
d.rounded_rectangle([30, 24, W-30, 92], radius=14, fill=HEAD2)
d.text((W//2, 58), "MVP CANVAS — Minha Agenda de Tarefas", font=font(34, True),
       fill=(255,255,255), anchor="mm")
d.text((W-44, 78), "TaskFlow Labs · Lean Inception", font=font(14), fill=(210,225,255), anchor="ra")

# ---- Proposta do MVP (faixa larga) ----
panel([30, 108, W-30, 250], "1 · Proposta do MVP (Visão)", [
    "Validar que profissionais autônomos, estudantes e pequenas equipes adotam um gerenciador de tarefas "
    "simples, gratuito e visual (Kanban) para organizar o dia a dia — em vez de planilhas, post-its ou "
    "ferramentas complexas (Trello/Asana/Notion).",
], tint=True)

# ---- Grade de 6 blocos ----
top = 266
colw = (W - 30 - 30 - 2*20) // 3
row_h = 350
gap = 20
x0 = 30
x1 = x0 + colw + gap
x2 = x1 + colw + gap

panel([x0, top, x0+colw, top+row_h], "2 · Personas Segmentadas", [
    "**Carla, a Autônoma", "Designer freelancer; organiza tarefas de vários clientes.",
    "**Rafael, o Estudante", "Acompanha entregas da faculdade e do estágio.",
    "**Marina, a Líder de equipe", "Acompanha tarefas por pessoa em time pequeno.",
])
panel([x1, top, x1+colw, top+row_h], "3 · Jornadas", [
    "**Organizar o dia", "Selecionar usuário → criar tarefas → mover entre colunas → concluir.",
    "**Acompanhar a equipe", "Alternar usuários → observar volume por coluna → redistribuir.",
])
panel([x2, top, x2+colw, top+row_h], "4 · Funcionalidades (MVP)", [
    "Cadastro e seleção de usuário",
    "Criar / listar / mover / excluir tarefa",
    "Quadro Kanban (3 colunas)",
    "Filtrar por status",
    "Sugerir tarefa (API externa)",
    "API REST documentada (Swagger)",
    "Responsividade (mobile)",
])

top2 = top + row_h + gap
panel([x0, top2, x0+colw, top2+row_h], "5 · Resultado Esperado (Hipótese)", [
    "**Hipótese", "Existe demanda por um gerenciador de tarefas minimalista e gratuito.",
    "**Aprendizado", "Entender se o Kanban simples basta para o dia a dia e se a simplicidade é "
    "percebida como vantagem (e não como falta de recursos).",
])
panel([x1, top2, x1+colw, top2+row_h], "6 · Métricas (validar hipótese)", [
    "**Ativação", "≥ 70% criam 1+ tarefa após cadastro.",
    "**Engajamento", "≥ 5 tarefas/usuário por semana.",
    "**Conclusão", "≥ 40% das tarefas chegam a 'Concluído'.",
    "**Retenção (7d)", "≥ 30% retornam em 7 dias.",
    "**Qualidade", "NPS ≥ 30.",
])
panel([x2, top2, x2+colw, top2+row_h], "7 · Custo & Cronograma", [
    "**Equipe", "5 pessoas (PO, SM/Dev, Dev Back, Dev Front, Designer part-time).",
    "**Cadência", "Sprints de 2 semanas.",
    "**Esforço do MVP", "3 sprints (~6 semanas).",
    "**Custo", "Horas do time + cloud de baixo custo (tier gratuito/básico).",
], tint=True)

img.save(os.path.join(OUT, "mvp-canvas.png"))
print("OK:", os.path.join(OUT, "mvp-canvas.png"))
