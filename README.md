# MVP — Minha Agenda de Tarefas
### Sprint de Gestão Ágil de Projetos e Produtos — PUC-Rio
**Autor:** Jackson Costa · Pós-graduação em Engenharia de Software

Entrega do MVP de um produto de software de livre escolha: **Minha Agenda de Tarefas**,
um gerenciador de tarefas web no estilo **Kanban** (colunas *A Fazer / Em Andamento /
Concluído*), simples, gratuito e responsivo. O produto foi delineado por meio de uma
**Lean Inception** completa, com backlog construído no padrão ágil e protótipos de baixa
fidelidade para a primeira sprint.

---

## 📦 Conteúdo da entrega

| Item | Onde está | Pontuação |
|------|-----------|:---------:|
| **Lean Inception + MVP Canvas** | [`canvas-url.txt`](canvas-url.txt) (URL Miro) · conteúdo em [`docs/lean-inception.md`](docs/lean-inception.md), [`docs/mvp-canvas.md`](docs/mvp-canvas.md) · imagem em [`assets/mvp-canvas.png`](assets/mvp-canvas.png) | 3,0 |
| **Backlog do Produto + DoR + DoD** | [`product-backlog.pdf`](product-backlog.pdf) · fonte Jira em [`jira-import/`](jira-import/) | 1,5 |
| **Backlog da Sprint 1** | [`sprint-backlog.pdf`](sprint-backlog.pdf) | 1,5 |
| **Protótipos (wireframes)** | [`wireframes/`](wireframes/) | 2,0 |
| **Vídeo de apresentação** | `apresentacao-mvp.mp4` ou `video-url.txt` — apoio: slides [`docs/apresentacao-slides.pptx`](docs/apresentacao-slides.pptx), narração [`docs/narracao.md`](docs/narracao.md), roteiro [`docs/video-roteiro.md`](docs/video-roteiro.md) | 2,0 |

---

## 🎯 O produto em uma frase
> **PARA** profissionais autônomos, estudantes e pequenas equipes **QUE** precisam
> organizar tarefas sem complexidade, o **Minha Agenda de Tarefas** é um gerenciador
> Kanban **QUE** permite criar, acompanhar e concluir tarefas de forma simples, visual e
> gratuita — **DIFERENTE DE** Trello/Asana/Notion, que são complexos e pagos.

## 👥 Cenário de negócio (resumo)
- **Empresa hipotética:** TaskFlow Labs (micro-startup de produtividade).
- **Stakeholders:** patrocinador, PO, usuários (autônomo, estudante, líder de equipe),
  time de dev, suporte/ops e DPO (LGPD).
- **Time Scrum enxuto (5 pessoas):** PO · Scrum Master/Dev · Dev Back-end · Dev Front-end
  · Designer UX/UI (part-time).

Detalhes completos em [`docs/lean-inception.md`](docs/lean-inception.md).

## 📁 Estrutura do repositório
```
mvp-gestao-agil/
├── README.md
├── canvas-url.txt              # URL do board do Miro (Lean Inception + MVP Canvas)
├── product-backlog.pdf         # Backlog do produto + DoR + DoD (com RNF)
├── sprint-backlog.pdf          # Backlog da Sprint 1 (detalhado, estimado, com critérios)
├── wireframes/                 # Protótipos de baixa fidelidade (Sprint 1)
│   ├── 01-selecao-cadastro-usuario.png
│   ├── 02-nova-tarefa.png
│   ├── 03-quadro-kanban.png
│   ├── 04-modal-exclusao.png
│   └── 05-mobile-responsivo.png
├── assets/
│   └── mvp-canvas.png          # MVP Canvas em imagem (para colar no Miro)
├── docs/
│   ├── lean-inception.md       # Todas as etapas da Lean Inception
│   ├── mvp-canvas.md           # Conteúdo do MVP Canvas
│   ├── apresentacao-slides.pptx # Slides de apoio para o vídeo
│   ├── narracao.md             # Texto de narração do vídeo
│   └── video-roteiro.md        # Roteiro do vídeo de showcase
└── jira-import/
    └── jira-backlog-import.csv # Backlog pronto para importar no Jira
```

---
Desenvolvido por **Jackson Costa** — PUC-Rio.
