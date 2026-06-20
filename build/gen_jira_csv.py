# -*- coding: utf-8 -*-
"""Gera jira-backlog-import.csv pronto para importação no Jira (CSV importer).

Mapeia épicos, features (como sub-épicos/labels), histórias, enablers e RNF.
Estratégia: Épicos como Epic; Features viram label + agrupamento; itens como Story/Task
com Epic Link apontando para o Summary do épico.
"""
import os, csv

import backlog_data as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "jira-import"))
os.makedirs(OUT, exist_ok=True)
path = os.path.join(OUT, "jira-backlog-import.csv")

MOSCOW_TO_PRIORITY = {
    "Must": "Highest", "Should": "High", "Could": "Medium",
    "Won't (agora)": "Lowest", "Must Have": "Highest",
}

TIPO_TO_ISSUETYPE = {
    "História": "Story",
    "Enabler": "Story",
    "Req. Não Funcional": "Story",
}

def prio(moscow):
    for k, v in MOSCOW_TO_PRIORITY.items():
        if k in moscow:
            return v
    return "Medium"

rows = []
# Cabeçalho
header = ["Issue Type", "Summary", "Epic Name", "Epic Link", "Story Points",
          "Priority", "Labels", "Sprint", "Description", "Acceptance Criteria"]

sprint_ids = set(D.SPRINT_BACKLOG_IDS)

for e in D.PRODUCT_BACKLOG:
    epic_summary = e["epico"]
    # Epic row
    rows.append(["Epic", epic_summary, epic_summary, "", "",
                 prio(e["prioridade"]), "MVP",
                 "", e["objetivo"], ""])
    for f in e["features"]:
        feat_label = f["nome"].split(" — ")[0].replace(".", "").replace("F", "Feature")
        for it in f["itens"]:
            ac = " \n".join(f"- {a}" for a in it["ac"])
            sp = it["sp"] if it["sp"] is not None else ""
            sprint = D.SPRINT_INFO["nome"] if it["id"] in sprint_ids else ""
            labels = f'{it["id"]} {it["tipo"].replace(" ", "-")}'
            rows.append([
                TIPO_TO_ISSUETYPE.get(it["tipo"], "Story"),
                f'{it["id"]} — {it["titulo"]}',
                "",
                epic_summary,
                sp,
                prio(it["prioridade"]),
                labels,
                sprint,
                f'[{f["nome"]}] {it["desc"]}',
                ac,
            ])

with open(path, "w", newline="", encoding="utf-8-sig") as fp:
    w = csv.writer(fp, delimiter=",", quoting=csv.QUOTE_ALL)
    w.writerow(header)
    w.writerows(rows)

print("OK:", path, "-", len(rows), "linhas")
