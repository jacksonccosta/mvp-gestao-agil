# -*- coding: utf-8 -*-
"""Fonte única de dados do backlog do produto e da sprint.

Consumido por gen_pdfs.py (gera os PDFs) e gen_jira_csv.py (gera o CSV do Jira).
"""

PROJETO = "Minha Agenda de Tarefas"
TIME = "TaskFlow Labs — Squad MVP (5 pessoas)"

# ---------------------------------------------------------------------------
# BACKLOG DO PRODUTO (emergente: MVP detalhado, incrementos mais grossos)
# ---------------------------------------------------------------------------

PRODUCT_BACKLOG = [
    {
        "epico": "EP1 — MVP: Minha Agenda de Tarefas",
        "objetivo": "Entregar o gerenciador de tarefas Kanban mínimo viável que permite "
                    "ao usuário cadastrar-se, criar, acompanhar, filtrar e concluir tarefas.",
        "prioridade": "Altíssima (Must Have)",
        "features": [
            {
                "nome": "F1.1 — Gestão de Usuários",
                "prioridade": "Alta",
                "itens": [
                    {"id": "US01", "tipo": "História",
                     "titulo": "Cadastrar usuário",
                     "desc": "Como visitante, quero cadastrar meu nome e e-mail para que minhas tarefas fiquem associadas a mim.",
                     "sp": 3, "prioridade": "Must",
                     "ac": ["Dado um nome e e-mail válidos, quando submeto o cadastro, então o usuário é criado e passa a aparecer no seletor.",
                            "Dado um e-mail já cadastrado, quando tento cadastrar novamente, então recebo mensagem de erro clara.",
                            "Dado um e-mail em formato inválido, quando submeto, então o sistema bloqueia e informa o erro."]},
                    {"id": "US02", "tipo": "História",
                     "titulo": "Selecionar/trocar usuário",
                     "desc": "Como usuário, quero selecionar meu usuário em uma lista para visualizar apenas as minhas tarefas.",
                     "sp": 2, "prioridade": "Must",
                     "ac": ["Dado que existem usuários cadastrados, quando abro a aplicação, então vejo a lista de usuários no seletor.",
                            "Dado que seleciono um usuário, quando a seleção é feita, então o quadro de tarefas daquele usuário é exibido."]},
                ],
            },
            {
                "nome": "F1.2 — Gestão de Tarefas (CRUD + Kanban)",
                "prioridade": "Altíssima",
                "itens": [
                    {"id": "US03", "tipo": "História",
                     "titulo": "Criar tarefa",
                     "desc": "Como usuário, quero criar uma tarefa com título e descrição para registrar algo que preciso fazer.",
                     "sp": 3, "prioridade": "Must",
                     "ac": ["Dado um título preenchido, quando crio a tarefa, então ela aparece na coluna 'A Fazer'.",
                            "Dado um título vazio, quando tento criar, então o sistema impede e informa que o título é obrigatório.",
                            "A descrição é opcional."]},
                    {"id": "US04", "tipo": "História",
                     "titulo": "Visualizar quadro Kanban",
                     "desc": "Como usuário, quero ver minhas tarefas organizadas em três colunas (A Fazer, Em Andamento, Concluído) para ter visão do meu progresso.",
                     "sp": 5, "prioridade": "Must",
                     "ac": ["Dado que possuo tarefas, quando abro o quadro, então cada tarefa aparece na coluna do seu status.",
                            "Dado que não possuo tarefas, quando abro o quadro, então vejo as colunas vazias sem erro.",
                            "Cada cartão exibe título, descrição e ações disponíveis."]},
                    {"id": "US05", "tipo": "História",
                     "titulo": "Mover/editar status da tarefa",
                     "desc": "Como usuário, quero mudar o status de uma tarefa para refletir o andamento do meu trabalho.",
                     "sp": 5, "prioridade": "Must",
                     "ac": ["Dado um cartão em 'A Fazer', quando altero seu status para 'Em Andamento', então ele passa para a coluna correspondente.",
                            "A alteração é persistida e permanece após recarregar a página.",
                            "Só o dono da tarefa consegue alterá-la."]},
                    {"id": "US06", "tipo": "História",
                     "titulo": "Excluir tarefa",
                     "desc": "Como usuário, quero excluir uma tarefa para remover itens que não preciso mais.",
                     "sp": 3, "prioridade": "Should",
                     "ac": ["Dado um cartão, quando clico em excluir, então é exibido um modal de confirmação.",
                            "Dado o modal de confirmação, quando confirmo, então a tarefa é removida do quadro e do banco.",
                            "Quando cancelo, então nada é removido."]},
                    {"id": "US07", "tipo": "História",
                     "titulo": "Filtrar tarefas por status",
                     "desc": "Como usuário, quero filtrar as tarefas por status para focar no que importa no momento.",
                     "sp": 3, "prioridade": "Should",
                     "ac": ["Dado o filtro 'Em Andamento', quando o aplico, então apenas tarefas em andamento são exibidas.",
                            "Dado o filtro 'Todos', quando o aplico, então todas as tarefas voltam a ser exibidas."]},
                ],
            },
            {
                "nome": "F1.3 — Produtividade Assistida",
                "prioridade": "Média",
                "itens": [
                    {"id": "US08", "tipo": "História",
                     "titulo": "Sugerir tarefa",
                     "desc": "Como usuário sem ideias, quero receber uma sugestão de tarefa para me ajudar a começar.",
                     "sp": 3, "prioridade": "Could",
                     "ac": ["Dado o botão 'Sugerir Tarefa', quando clico, então recebo uma sugestão vinda de uma API externa.",
                            "Dado falha na API externa, quando ocorre o erro, então recebo uma mensagem amigável sem quebrar a aplicação."]},
                ],
            },
            {
                "nome": "F1.4 — Plataforma & Qualidade (Enablers e Requisitos Não Funcionais)",
                "prioridade": "Alta",
                "itens": [
                    {"id": "EN01", "tipo": "Enabler",
                     "titulo": "API REST documentada (Swagger)",
                     "desc": "Como time de desenvolvimento, queremos uma API REST documentada via Swagger para padronizar a integração front-back e facilitar testes.",
                     "sp": 3, "prioridade": "Must",
                     "ac": ["A API expõe endpoints REST para usuários e tarefas.",
                            "A documentação Swagger está acessível em /apidocs e cobre todos os endpoints.",
                            "Há testes automatizados (PyTest) dos principais fluxos."]},
                    {"id": "EN02", "tipo": "Enabler",
                     "titulo": "Responsividade e layout base (Bootstrap)",
                     "desc": "Como time, queremos um layout responsivo base para que a aplicação funcione bem em desktop e mobile.",
                     "sp": 3, "prioridade": "Should",
                     "ac": ["A aplicação se adapta a telas de 360px a 1920px sem quebra de layout.",
                            "As colunas do Kanban se reorganizam em telas pequenas."]},
                    {"id": "NFR01", "tipo": "Req. Não Funcional",
                     "titulo": "Desempenho do quadro de tarefas",
                     "desc": "Como usuário, quero que o quadro de tarefas carregue em até 2 segundos para uma experiência fluida.",
                     "sp": 2, "prioridade": "Must",
                     "ac": ["Com até 100 tarefas, o tempo de resposta da listagem é ≤ 2s em conexão 4G.",
                            "As chamadas à API retornam em ≤ 500ms no percentil 95 em ambiente de homologação."]},
                ],
            },
        ],
    },
    {
        "epico": "EP2 — Incremento 1: Conta e Planejamento",
        "objetivo": "Evoluir o produto com autenticação real e planejamento temporal das tarefas.",
        "prioridade": "Média (pós-MVP)",
        "features": [
            {
                "nome": "F2.1 — Autenticação de Usuário",
                "prioridade": "Média",
                "itens": [
                    {"id": "US09", "tipo": "História",
                     "titulo": "Login com e-mail e senha",
                     "desc": "Como usuário, quero autenticar com e-mail e senha para que apenas eu acesse minhas tarefas.",
                     "sp": None, "prioridade": "Should",
                     "ac": ["(A detalhar no refinamento) — proteger acesso às tarefas por sessão autenticada."]},
                ],
            },
            {
                "nome": "F2.2 — Planejamento Temporal",
                "prioridade": "Média",
                "itens": [
                    {"id": "US10", "tipo": "História",
                     "titulo": "Data de vencimento da tarefa",
                     "desc": "Como usuário, quero definir uma data de vencimento para priorizar minhas tarefas.",
                     "sp": None, "prioridade": "Could",
                     "ac": ["(A detalhar no refinamento)."]},
                    {"id": "US11", "tipo": "História",
                     "titulo": "Edição completa da tarefa",
                     "desc": "Como usuário, quero editar título e descrição de uma tarefa existente para corrigir informações.",
                     "sp": None, "prioridade": "Could",
                     "ac": ["(A detalhar no refinamento)."]},
                ],
            },
        ],
    },
    {
        "epico": "EP3 — Incremento 2: Organização Avançada",
        "objetivo": "Adicionar recursos de organização e engajamento (não refinado — backlog emergente).",
        "prioridade": "Baixa (futuro)",
        "features": [
            {
                "nome": "F3.1 — Organização e Engajamento",
                "prioridade": "Baixa",
                "itens": [
                    {"id": "US12", "tipo": "História", "titulo": "Etiquetas/categorias", "desc": "Como usuário, quero etiquetar tarefas para agrupá-las por contexto.", "sp": None, "prioridade": "Won't (agora)", "ac": ["(Não refinado)."]},
                    {"id": "US13", "tipo": "História", "titulo": "Modo escuro", "desc": "Como usuário, quero alternar para o modo escuro por conforto visual.", "sp": None, "prioridade": "Won't (agora)", "ac": ["(Não refinado)."]},
                    {"id": "US14", "tipo": "História", "titulo": "Notificações", "desc": "Como usuário, quero ser notificado de tarefas próximas do vencimento.", "sp": None, "prioridade": "Won't (agora)", "ac": ["(Não refinado)."]},
                    {"id": "US15", "tipo": "História", "titulo": "Compartilhamento de quadro", "desc": "Como líder, quero compartilhar um quadro com minha equipe.", "sp": None, "prioridade": "Won't (agora)", "ac": ["(Não refinado)."]},
                ],
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# DEFINITION OF READY / DEFINITION OF DONE
# ---------------------------------------------------------------------------

DEFINITION_OF_READY = [
    "A história está escrita no formato 'Como [persona], quero [objetivo] para [benefício]'.",
    "A história é independente, pequena o suficiente para caber em uma sprint e testável (INVEST).",
    "Possui critérios de aceitação claros (formato Dado/Quando/Então).",
    "Possui estimativa relativa em story points, acordada pelo time no Planning Poker.",
    "As dependências técnicas e de negócio foram identificadas e não bloqueiam o início.",
    "Os protótipos/wireframes necessários estão disponíveis (quando houver impacto de UI).",
    "A prioridade foi definida pelo Product Owner (MoSCoW).",
    "O time entende o valor de negócio e não há dúvidas impeditivas.",
]

DEFINITION_OF_DONE = [
    "Código implementado, revisado por par (code review) e integrado à branch principal.",
    "Todos os critérios de aceitação da história foram atendidos e validados pelo PO.",
    "Testes automatizados (PyTest) escritos e passando; sem regressões na suíte.",
    "Funcionalidade testada em desktop e mobile (responsividade verificada).",
    "[RNF — Desempenho] O carregamento do quadro de tarefas ocorre em ≤ 2 segundos com até 100 tarefas.",
    "[RNF — Usabilidade] Mensagens de erro são claras e a aplicação não quebra em falhas externas.",
    "[RNF — Segurança/LGPD] Dados pessoais (nome/e-mail) trafegam de forma segura e validados no servidor.",
    "Documentação da API (Swagger) atualizada quando há mudança de contrato.",
    "Nenhum bug crítico ou bloqueante em aberto relacionado à história.",
    "Deploy realizado em ambiente de homologação e demonstrável na Sprint Review.",
]

# ---------------------------------------------------------------------------
# BACKLOG DA SPRINT 1
# ---------------------------------------------------------------------------

SPRINT_INFO = {
    "nome": "Sprint 1",
    "duracao": "2 semanas",
    "objetivo": "Permitir que o usuário se cadastre, selecione seu perfil, crie tarefas e "
                "as visualize/movimente no quadro Kanban — entregando o fluxo central do produto "
                "ponta a ponta, sustentado por uma API REST documentada.",
    "capacidade": "26 story points (velocidade estimada inicial do squad de 5 pessoas em 2 semanas).",
}

# Itens selecionados para a Sprint 1 (já atendem ao Definition of Ready)
SPRINT_BACKLOG_IDS = ["EN01", "US01", "US02", "US03", "US04", "US05"]
