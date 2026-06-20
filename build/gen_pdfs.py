# -*- coding: utf-8 -*-
"""Gera product-backlog.pdf e sprint-backlog.pdf a partir de backlog_data.py."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, ListFlowable, ListItem, PageBreak
)

import backlog_data as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Paleta (alinhada ao tema "info/azul" do produto)
AZUL = colors.HexColor("#0d6efd")
AZUL_ESC = colors.HexColor("#0a4fb0")
CIANO = colors.HexColor("#0dcaf0")
CINZA = colors.HexColor("#f1f3f5")
CINZA_TXT = colors.HexColor("#495057")
VERDE = colors.HexColor("#198754")
AMARELO = colors.HexColor("#ffc107")
ROXO = colors.HexColor("#6f42c1")

styles = getSampleStyleSheet()

def S(name, **kw):
    base = kw.pop("parent", styles["Normal"])
    return ParagraphStyle(name, parent=base, **kw)

st_capa_titulo = S("capaT", fontName="Helvetica-Bold", fontSize=26, leading=32,
                   textColor=AZUL_ESC, alignment=TA_CENTER, spaceAfter=10)
st_capa_sub = S("capaS", fontName="Helvetica", fontSize=14, leading=20,
                textColor=CINZA_TXT, alignment=TA_CENTER)
st_h1 = S("h1", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=colors.white)
st_h2 = S("h2", fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=AZUL_ESC,
          spaceBefore=10, spaceAfter=4)
st_body = S("body", fontSize=9.5, leading=13, textColor=colors.HexColor("#212529"))
st_body_w = S("bodyw", fontSize=10, leading=14, textColor=colors.white)
st_small = S("small", fontSize=8.5, leading=11, textColor=CINZA_TXT)
st_cell = S("cell", fontSize=8.8, leading=11.5)
st_cell_b = S("cellb", fontSize=8.8, leading=11.5, fontName="Helvetica-Bold")
st_ac = S("ac", fontSize=8.5, leading=11, leftIndent=6)
st_meta = S("meta", fontSize=9, leading=13, textColor=CINZA_TXT)


def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    # rodapé
    canvas.setStrokeColor(colors.HexColor("#dee2e6"))
    canvas.line(2*cm, 1.4*cm, w-2*cm, 1.4*cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(CINZA_TXT)
    canvas.drawString(2*cm, 1.05*cm, f"{D.PROJETO} — {doc.titulo_doc}")
    canvas.drawRightString(w-2*cm, 1.05*cm, f"Página {doc.page}")
    canvas.restoreState()


def make_doc(path, titulo_doc):
    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=2*cm, rightMargin=2*cm,
                          topMargin=1.8*cm, bottomMargin=1.8*cm,
                          title=titulo_doc, author="Jackson Costa")
    doc.titulo_doc = titulo_doc
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame],
                                       onPage=header_footer)])
    return doc


def banner(text, bg, sub=None):
    """Faixa colorida de cabeçalho (épico/seção)."""
    cells = [[Paragraph(text, st_h1)]]
    if sub:
        cells.append([Paragraph(sub, st_body_w)])
    t = Table(cells, colWidths=[doc_width])
    style = [("BACKGROUND", (0,0), (-1,-1), bg),
             ("LEFTPADDING", (0,0), (-1,-1), 10),
             ("RIGHTPADDING", (0,0), (-1,-1), 10),
             ("TOPPADDING", (0,0), (-1,-1), 7),
             ("BOTTOMPADDING", (0,0), (-1,-1), 7)]
    t.setStyle(TableStyle(style))
    return t

doc_width = A4[0] - 4*cm

TIPO_COR = {"História": AZUL, "Enabler": ROXO, "Req. Não Funcional": VERDE,
            "Épico": AZUL_ESC}


def chip(text, color):
    t = Table([[Paragraph(f'<font color="white"><b>{text}</b></font>', st_small)]],
              colWidths=[2.6*cm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),color),
                           ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
                           ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2)]))
    return t


def item_card(it, full=True):
    """Cartão de um item de backlog (história/enabler/RNF)."""
    cor = TIPO_COR.get(it["tipo"], AZUL)
    sp = it["sp"]
    sp_txt = f'{sp} SP' if sp is not None else '—'
    header = Table([[
        Paragraph(f'<font color="white"><b>{it["id"]} · {it["titulo"]}</b></font>', st_body_w),
        Paragraph(f'<font color="white">{it["tipo"]} · {sp_txt} · {it["prioridade"]}</font>', st_small),
    ]], colWidths=[doc_width*0.62, doc_width*0.38])
    header.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),cor),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("ALIGN",(1,0),(1,0),"RIGHT"),
        ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
    ]))
    rows = [[header]]
    body = [Paragraph(f'<b>Descrição:</b> {it["desc"]}', st_body)]
    if full:
        body.append(Spacer(1, 4))
        body.append(Paragraph('<b>Critérios de aceitação:</b>', st_body))
        body.append(ListFlowable(
            [ListItem(Paragraph(a, st_ac), leftIndent=10) for a in it["ac"]],
            bulletType="bullet", start="•", leftIndent=10))
    inner = Table([[body]], colWidths=[doc_width])
    inner.setStyle(TableStyle([
        ("BOX",(0,0),(-1,-1),0.6,colors.HexColor("#dee2e6")),
        ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
    ]))
    rows.append([inner])
    wrap = Table(rows, colWidths=[doc_width])
    wrap.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                              ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
    return KeepTogether([wrap, Spacer(1, 6)])


def capa(titulo, subtitulo, extra_lines):
    el = [Spacer(1, 4.5*cm),
          Paragraph(D.PROJETO, st_capa_titulo),
          Spacer(1, 0.3*cm),
          HRFlowable(width="40%", thickness=2, color=CIANO, hAlign="CENTER"),
          Spacer(1, 0.6*cm),
          Paragraph(titulo, S("ct2", fontName="Helvetica-Bold", fontSize=18,
                              textColor=AZUL, alignment=TA_CENTER)),
          Spacer(1, 0.3*cm),
          Paragraph(subtitulo, st_capa_sub),
          Spacer(1, 2.5*cm)]
    for line in extra_lines:
        el.append(Paragraph(line, S("cx", fontSize=11, leading=18,
                                    textColor=CINZA_TXT, alignment=TA_CENTER)))
    el.append(PageBreak())
    return el


def def_list_block(titulo, itens, cor):
    out = [banner(titulo, cor), Spacer(1, 6)]
    out.append(ListFlowable(
        [ListItem(Paragraph(x, st_body), leftIndent=12, value=i+1)
         for i, x in enumerate(itens)],
        bulletType="1", leftIndent=14))
    out.append(Spacer(1, 10))
    return out


# ===========================================================================
# PRODUCT BACKLOG PDF
# ===========================================================================
def build_product_backlog():
    path = os.path.join(OUT, "product-backlog.pdf")
    doc = make_doc(path, "Backlog do Produto")
    el = []
    el += capa("Backlog do Produto",
               "Épicos · Features · Histórias de Usuário · Enablers · RNF",
               ["<b>Autor:</b> Jackson Costa — PUC-Rio",
                f"<b>Time:</b> {D.TIME}",
                "<b>Ferramenta de gestão:</b> Jira (export incluso em /jira-import)",
                "<b>Disciplina:</b> Gestão Ágil de Projetos e Produtos"])

    el.append(Paragraph("Visão geral do backlog", st_h2))
    el.append(Paragraph(
        "Backlog <b>emergente</b>: os itens do MVP (EP1) estão detalhados com estimativas e "
        "critérios de aceitação; os incrementos seguintes (EP2 e EP3) permanecem em granularidade "
        "mais grossa, a serem refinados conforme a prioridade. A priorização segue <b>MoSCoW</b> "
        "(Must/Should/Could/Won't).", st_body))
    el.append(Spacer(1, 6))

    # tabela resumo de épicos
    head = ["Épico", "Prioridade", "Itens"]
    data = [[Paragraph(f'<b>{e["epico"]}</b>', st_cell),
             Paragraph(e["prioridade"], st_cell),
             Paragraph(str(sum(len(f["itens"]) for f in e["features"])), st_cell)]
            for e in D.PRODUCT_BACKLOG]
    t = Table([head]+data, colWidths=[doc_width*0.6, doc_width*0.27, doc_width*0.13])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),AZUL_ESC),("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,0),9),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, CINZA]),
        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#dee2e6")),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("ALIGN",(2,0),(2,-1),"CENTER"),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("LEFTPADDING",(0,0),(-1,-1),7),
    ]))
    el.append(t)
    el.append(PageBreak())

    cores_epico = [AZUL_ESC, ROXO, CINZA_TXT]
    for idx, e in enumerate(D.PRODUCT_BACKLOG):
        cor = cores_epico[idx % len(cores_epico)]
        el.append(banner(e["epico"], cor,
                         f'Objetivo: {e["objetivo"]}  ·  Prioridade: {e["prioridade"]}'))
        el.append(Spacer(1, 8))
        for f in e["features"]:
            el.append(Paragraph(f'▸ <b>{f["nome"]}</b> '
                                f'<font color="#868e96" size="8">(prioridade: {f["prioridade"]})</font>',
                                st_h2))
            full = (idx == 0)  # detalha só o MVP; incrementos em granularidade grossa
            for it in f["itens"]:
                el.append(item_card(it, full=full))
        el.append(Spacer(1, 6))
        if idx < len(D.PRODUCT_BACKLOG)-1:
            el.append(PageBreak())

    # DoR e DoD
    el.append(PageBreak())
    el += def_list_block("Definition of Ready (DoR)", D.DEFINITION_OF_READY, VERDE)
    el.append(Spacer(1, 8))
    el += def_list_block("Definition of Done (DoD)", D.DEFINITION_OF_DONE, AZUL)
    el.append(Spacer(1, 6))
    el.append(Paragraph(
        "<b>Nota:</b> o Definition of Done inclui requisitos não funcionais explícitos "
        "(desempenho, usabilidade e segurança/LGPD), conforme exigido na gestão do backlog.",
        st_small))

    doc.build(el)
    return path


# ===========================================================================
# SPRINT BACKLOG PDF
# ===========================================================================
def find_item(item_id):
    for e in D.PRODUCT_BACKLOG:
        for f in e["features"]:
            for it in f["itens"]:
                if it["id"] == item_id:
                    return it, f, e
    raise KeyError(item_id)


def build_sprint_backlog():
    path = os.path.join(OUT, "sprint-backlog.pdf")
    doc = make_doc(path, "Backlog da Sprint 1")
    info = D.SPRINT_INFO
    itens = [find_item(i)[0] for i in D.SPRINT_BACKLOG_IDS]
    total_sp = sum(i["sp"] for i in itens if i["sp"])

    el = []
    el += capa("Backlog da Sprint 1",
               "Histórias detalhadas · Estimadas · Com critérios de aceitação",
               ["<b>Autor:</b> Jackson Costa — PUC-Rio",
                f"<b>Time:</b> {D.TIME}",
                f"<b>Duração:</b> {info['duracao']}",
                f"<b>Total comprometido:</b> {total_sp} story points"])

    # Meta da Sprint
    el.append(banner("Meta da Sprint (Sprint Goal)", AZUL))
    el.append(Spacer(1, 6))
    el.append(Paragraph(info["objetivo"], st_body))
    el.append(Spacer(1, 8))
    meta_tbl = Table([
        [Paragraph("<b>Sprint</b>", st_cell), Paragraph(info["nome"], st_cell),
         Paragraph("<b>Duração</b>", st_cell), Paragraph(info["duracao"], st_cell)],
        [Paragraph("<b>Capacidade</b>", st_cell), Paragraph(info["capacidade"], st_cell),
         Paragraph("<b>Comprometido</b>", st_cell), Paragraph(f"{total_sp} SP", st_cell)],
    ], colWidths=[doc_width*0.16, doc_width*0.34, doc_width*0.18, doc_width*0.32])
    meta_tbl.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#dee2e6")),
        ("BACKGROUND",(0,0),(0,-1),CINZA),("BACKGROUND",(2,0),(2,-1),CINZA),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("LEFTPADDING",(0,0),(-1,-1),7),
    ]))
    el.append(meta_tbl)
    el.append(Spacer(1, 12))

    # Tabela-resumo dos itens
    el.append(Paragraph("Itens selecionados para a Sprint 1", st_h2))
    head = ["ID", "Item", "Tipo", "SP", "Prioridade"]
    rows = [[Paragraph(f'<b>{it["id"]}</b>', st_cell), Paragraph(it["titulo"], st_cell),
             Paragraph(it["tipo"], st_cell), Paragraph(str(it["sp"]), st_cell),
             Paragraph(it["prioridade"], st_cell)] for it in itens]
    rows.append([Paragraph("", st_cell), Paragraph("<b>TOTAL</b>", st_cell_b),
                 Paragraph("", st_cell), Paragraph(f"<b>{total_sp}</b>", st_cell_b),
                 Paragraph("", st_cell)])
    t = Table([head]+rows, colWidths=[doc_width*0.1, doc_width*0.46, doc_width*0.2,
                                      doc_width*0.08, doc_width*0.16])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),AZUL),("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
        ("ROWBACKGROUNDS",(0,1),(-1,-2),[colors.white, CINZA]),
        ("BACKGROUND",(0,-1),(-1,-1),colors.HexColor("#e7f1ff")),
        ("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#dee2e6")),
        ("ALIGN",(3,0),(3,-1),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),6),
    ]))
    el.append(t)
    el.append(PageBreak())

    # Detalhe de cada história
    el.append(banner("Detalhamento das histórias (atendem ao Definition of Ready)", AZUL_ESC))
    el.append(Spacer(1, 10))
    for it in itens:
        el.append(item_card(it, full=True))
    el.append(Spacer(1, 8))
    el.append(Paragraph(
        "Todos os itens acima atendem ao <b>Definition of Ready</b>: estão no formato de história, "
        "são testáveis, possuem estimativa em story points e critérios de aceitação claros.",
        st_small))

    doc.build(el)
    return path


if __name__ == "__main__":
    p1 = build_product_backlog()
    p2 = build_sprint_backlog()
    print("OK:", p1)
    print("OK:", p2)
