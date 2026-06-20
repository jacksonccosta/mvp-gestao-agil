# Lean Inception — Minha Agenda de Tarefas

> Produto de software escolhido: **Minha Agenda de Tarefas** — uma aplicação web de
> gestão de tarefas no estilo Kanban (colunas *A Fazer*, *Em Andamento* e *Concluído*),
> com cadastro de usuários, CRUD de tarefas, filtros por status e sugestão automática
> de tarefas. Este documento registra **todas as etapas da Lean Inception** conduzidas
> para delinear o MVP, conforme o template do Caroli/Miroverse.

---

## 0. Contexto de Negócio (cenário hipotético)

A **TaskFlow Labs** é uma micro-startup que desenvolve ferramentas de produtividade
pessoal e para pequenas equipes. Foi identificada uma dor recorrente entre
profissionais autônomos, estudantes e pequenas equipes: as ferramentas de gestão de
tarefas existentes (Trello, Asana, Notion) são poderosas, porém **complexas demais para
quem só precisa organizar o dia a dia**, exigem curva de aprendizado e, muitas vezes,
planos pagos. A TaskFlow Labs quer lançar um produto **simples, gratuito e direto ao
ponto**, validando a hipótese de que existe demanda por um gerenciador "minimalista"
de tarefas com visão Kanban.

### Stakeholders, Usuários e Clientes

| Categoria | Quem | Interesse / Expectativa |
|-----------|------|--------------------------|
| **Patrocinador (Sponsor)** | Sócio-investidor da TaskFlow Labs | Validar a hipótese de produto com o menor investimento possível; ver tração de uso. |
| **Product Owner** | Gestora de Produto da TaskFlow Labs | Maximizar valor entregue por sprint; garantir aderência à visão. |
| **Usuário final primário** | Profissional autônomo / estudante | Organizar tarefas pessoais de forma rápida, sem fricção, em qualquer dispositivo. |
| **Usuário final secundário** | Pequena equipe (2 a 5 pessoas) | Acompanhar o andamento de tarefas por pessoa. |
| **Cliente (quem decide adotar)** | O próprio usuário (B2C) e líderes de pequenas equipes | Adotar uma ferramenta gratuita e simples que substitua planilhas/post-its. |
| **Time de Desenvolvimento** | Equipe Scrum enxuta (ver abaixo) | Construir incrementos de qualidade dentro do prazo. |
| **Área de Suporte/Ops** | Pessoa de DevOps/Suporte (acumulada) | Garantir disponibilidade, deploy e atendimento de incidentes. |
| **Regulação/LGPD** | Encarregado de dados (DPO terceirizado) | Garantir tratamento adequado de dados pessoais (nome, e-mail). |

### Time Scrum (equipe enxuta — 5 pessoas)

Equipe mínima viável para entregar o MVP com qualidade em um tempo razoável:

| Papel | Pessoas | Habilidades principais |
|-------|---------|------------------------|
| **Product Owner (PO)** | 1 | Visão de produto, priorização de backlog, escrita de histórias, contato com stakeholders. |
| **Scrum Master / Dev** | 1 | Facilitação ágil, remoção de impedimentos; atua também como desenvolvedor(a) full-stack part-time. |
| **Dev Back-end** | 1 | Python, Flask, SQLAlchemy, modelagem de dados, API REST, testes (PyTest). |
| **Dev Front-end** | 1 | HTML/CSS, Bootstrap, JavaScript, consumo de API, responsividade. |
| **Designer UX/UI (part-time)** | 1 | Pesquisa com usuário, wireframes/protótipos no Figma, design system, acessibilidade. |

> Time total: **5 pessoas**. O papel de QA é compartilhado entre os desenvolvedores
> (testes automatizados + testes exploratórios), e o de DevOps é acumulado pelo Dev
> Back-end. Essa composição mantém a equipe enxuta sem comprometer as competências
> essenciais ao MVP.

---

## Etapa 1 — Visão do Produto (Product Vision)

Construída com o template de Geoffrey Moore (elevator pitch):

> **PARA** profissionais autônomos, estudantes e pequenas equipes
> **QUE** precisam organizar suas tarefas do dia a dia sem complexidade,
> **O** Minha Agenda de Tarefas **É UM** gerenciador de tarefas web no estilo Kanban
> **QUE** permite criar, acompanhar e concluir tarefas de forma simples, visual e gratuita.
> **DIFERENTE DE** Trello, Asana e Notion, que são poderosos porém complexos e com planos pagos,
> **O NOSSO PRODUTO** é minimalista, gratuito, sem curva de aprendizado e funciona em qualquer dispositivo.

---

## Etapa 2 — É / Não É / Faz / Não Faz (The Product Is / Is Not / Does / Does Not)

| | Descrição |
|---|---|
| **É** | Um gerenciador de tarefas pessoal/leve, web, com visão Kanban, gratuito e minimalista. |
| **NÃO É** | Uma ferramenta corporativa de gestão de projetos (não substitui Jira); não é uma rede social; não é um app de calendário. |
| **FAZ** | Cadastra usuários; cria, edita, lista, filtra e exclui tarefas; move tarefas entre status; sugere tarefas. |
| **NÃO FAZ** | Não gerencia times grandes, não tem permissões/papéis avançados, não tem integrações externas complexas, não tem cobrança/billing. |

---

## Etapa 3 — Personas

### Persona 1 — Carla, a Autônoma (usuária primária)
- **28 anos, designer freelancer.** Trabalha de casa, gerencia vários clientes.
- **Necessidade:** ver rapidamente o que precisa fazer hoje e o que já entregou.
- **Dores:** perde post-its; Trello é "demais" para o que precisa; esquece tarefas.
- **Objetivo:** organizar o dia em menos de 1 minuto.

### Persona 2 — Rafael, o Estudante (usuário primário)
- **21 anos, universitário.** Concilia faculdade, estágio e projetos.
- **Necessidade:** acompanhar entregas de disciplinas e do estágio.
- **Dores:** procrastinação; falta de visão do progresso.
- **Objetivo:** visualizar o progresso e sentir-se motivado ao concluir tarefas.

### Persona 3 — Marina, a Líder de Pequena Equipe (usuária secundária)
- **35 anos, dona de um pequeno escritório de arquitetura (4 pessoas).**
- **Necessidade:** acompanhar tarefas por pessoa da equipe.
- **Dores:** não sabe quem está sobrecarregado; reuniões longas de alinhamento.
- **Objetivo:** ter visão rápida do andamento por usuário.

---

## Etapa 4 — Jornadas do Usuário (User Journeys)

### Jornada da Carla — "Organizar o dia"
1. Abre a aplicação no navegador.
2. Seleciona seu usuário (ou cadastra na primeira vez).
3. Visualiza o quadro Kanban com suas tarefas.
4. Cria as tarefas do dia (ou usa "Sugerir Tarefa" quando está sem ideias).
5. Move tarefas de *A Fazer* → *Em Andamento* conforme começa a trabalhar.
6. Ao concluir, move para *Concluído* e sente a sensação de progresso.

### Jornada da Marina — "Acompanhar a equipe"
1. Abre a aplicação.
2. Alterna entre os usuários da equipe pelo seletor.
3. Para cada pessoa, observa o volume em cada coluna.
4. Identifica quem está sobrecarregado e redistribui verbalmente.

---

## Etapa 5 — Brainstorming de Funcionalidades (Feature Brainstorming)

Funcionalidades levantadas por todo o time, agrupadas por jornada:

- Cadastro de usuário (nome + e-mail)
- Seleção/troca de usuário
- Criar tarefa (título + descrição)
- Listar tarefas do usuário em quadro Kanban
- Mover tarefa entre status (A Fazer / Em Andamento / Concluído)
- Editar status da tarefa
- Excluir tarefa (com confirmação)
- Filtrar tarefas por status
- Sugerir tarefa (integração com API externa de sugestões)
- Documentação da API (Swagger)
- Validação de dados e tratamento de erros
- Responsividade (mobile)
- Autenticação/login (futuro)
- Datas de vencimento e lembretes (futuro)
- Etiquetas/categorias (futuro)
- Compartilhamento de quadros (futuro)
- Notificações (futuro)
- Modo escuro (futuro)

---

## Etapa 6 — Revisão Técnica, de Negócio e UX (Technical, Business & UX Review)

Cada funcionalidade foi avaliada em três dimensões (Alto/Médio/Baixo):

| Funcionalidade | Esforço Técnico | Valor de Negócio | Valor UX |
|----------------|:---------------:|:----------------:|:--------:|
| Cadastro de usuário | Baixo | Alto | Médio |
| Seleção/troca de usuário | Baixo | Alto | Alto |
| Criar tarefa | Baixo | Alto | Alto |
| Quadro Kanban (listar) | Médio | Alto | Alto |
| Mover/editar status | Médio | Alto | Alto |
| Excluir tarefa | Baixo | Médio | Médio |
| Filtrar por status | Baixo | Médio | Alto |
| Sugerir tarefa (API externa) | Médio | Médio | Médio |
| Documentação Swagger | Baixo | Médio (técnico) | Baixo |
| Responsividade mobile | Médio | Alto | Alto |
| Autenticação/login | Alto | Médio | Médio |
| Datas/lembretes | Alto | Médio | Alto |

---

## Etapa 7 — Sequenciador de Funcionalidades (Sequencer) e definição do MVP

As funcionalidades foram dispostas em ondas de entrega. A **primeira onda** (linha do MVP)
contém o **menor conjunto de funcionalidades que entrega valor end-to-end** e permite
validar a hipótese central: *"usuários querem um gerenciador de tarefas simples no estilo Kanban"*.

| Onda | Funcionalidades |
|------|------------------|
| **MVP (Onda 1)** | Cadastro de usuário · Seleção de usuário · Criar tarefa · Quadro Kanban (listar) · Mover/editar status · Excluir tarefa · Filtrar por status · Sugerir tarefa · Documentação Swagger · Responsividade básica |
| **Incremento 1 (Onda 2)** | Autenticação/login · Datas de vencimento · Edição completa da tarefa (título/descrição) |
| **Incremento 2 (Onda 3)** | Etiquetas/categorias · Notificações · Modo escuro · Compartilhamento de quadros |

> A linha que separa a Onda 1 das demais é a **linha do MVP**: tudo acima dela compõe o
> produto mínimo viável a ser construído e validado.

---

## Etapa 8 — Canvas MVP (resultado)

O resultado consolidado da Lean Inception é o **MVP Canvas** (ver `mvp-canvas.md` e a
imagem em `../assets/mvp-canvas.png`). Ele sintetiza: proposta do MVP, personas
segmentadas, jornadas, funcionalidades, resultado esperado, métricas, custo/cronograma
e hipóteses a validar.

---

## Resumo das etapas executadas

1. ✅ Contexto de negócio (stakeholders + time Scrum)
2. ✅ Visão do produto
3. ✅ É / Não é / Faz / Não faz
4. ✅ Personas
5. ✅ Jornadas do usuário
6. ✅ Brainstorming de funcionalidades
7. ✅ Revisão técnica/negócio/UX
8. ✅ Sequenciador e definição do MVP
9. ✅ MVP Canvas

> Todas as etapas acima foram registradas no board do Miro (ver `../canvas-url.txt`).
