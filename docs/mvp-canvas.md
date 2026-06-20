# MVP Canvas — Minha Agenda de Tarefas

> Síntese final da Lean Inception. Este conteúdo deve ser transposto para o board do
> Miro (template Lean Inception). Há também uma versão em imagem em
> `../assets/mvp-canvas.png` pronta para colar no Miro.

---

### 1. Proposta do MVP (Visão)
Validar que profissionais autônomos, estudantes e pequenas equipes adotam um
gerenciador de tarefas **simples, gratuito e visual (Kanban)** para organizar o dia a
dia, em vez de planilhas, post-its ou ferramentas complexas.

### 2. Personas Segmentadas
- **Carla, a Autônoma** — organiza tarefas de múltiplos clientes.
- **Rafael, o Estudante** — acompanha entregas da faculdade e estágio.
- **Marina, a Líder de pequena equipe** — acompanha tarefas por pessoa.

### 3. Jornadas
- **Organizar o dia:** selecionar usuário → criar tarefas → mover entre colunas → concluir.
- **Acompanhar a equipe:** alternar usuários → observar volume por coluna → redistribuir.

### 4. Funcionalidades (o que será construído no MVP)
- Cadastro e seleção de usuário
- Criar tarefa (título + descrição)
- Quadro Kanban com 3 colunas (A Fazer / Em Andamento / Concluído)
- Mover/editar status da tarefa
- Excluir tarefa (com confirmação)
- Filtrar tarefas por status
- Sugerir tarefa (API externa)
- Documentação da API (Swagger)
- Responsividade básica (mobile)

### 5. Resultado Esperado (o que aprendemos / hipótese)
- **Hipótese:** existe demanda por um gerenciador de tarefas minimalista e gratuito.
- **Aprendizado esperado:** entender se o fluxo Kanban simples é suficiente para o dia a dia
  do usuário, e se a simplicidade é percebida como vantagem (e não como falta de recursos).

### 6. Métricas para validar a hipótese
- **Ativação:** % de usuários que criam ao menos 1 tarefa após o cadastro (meta ≥ 70%).
- **Engajamento:** nº médio de tarefas criadas por usuário/semana (meta ≥ 5).
- **Conclusão (valor entregue):** % de tarefas que chegam a *Concluído* (meta ≥ 40%).
- **Retenção:** % de usuários que retornam em 7 dias (meta ≥ 30%).
- **Qualidade percebida:** NPS pós-uso (meta ≥ 30).

### 7. Custo & Cronograma
- **Equipe:** 5 pessoas (PO, SM/Dev, Dev Back-end, Dev Front-end, Designer part-time).
- **Cadência:** Sprints de 2 semanas.
- **Esforço estimado do MVP:** 3 sprints (~6 semanas).
- **Custo principal:** horas da equipe + hospedagem cloud de baixo custo (tier gratuito/básico).

### 8. Hipóteses e Riscos a validar
- Usuários preferem simplicidade a quantidade de recursos. *(risco: acharem "simples demais")*
- O fluxo Kanban de 3 colunas cobre a maioria dos casos de uso pessoais.
- A ausência de login (seleção de usuário) é aceitável no MVP. *(risco de privacidade — mitigar no Incremento 1)*

---

## Tabela-resumo do Canvas (formato Miro)

| Bloco | Conteúdo-chave |
|-------|----------------|
| **Proposta do MVP** | Gerenciador de tarefas simples, gratuito e visual (Kanban). |
| **Personas** | Carla (autônoma), Rafael (estudante), Marina (líder de equipe). |
| **Jornadas** | Organizar o dia · Acompanhar a equipe. |
| **Funcionalidades** | Usuários, CRUD de tarefas, Kanban, filtro, sugestão, Swagger, responsivo. |
| **Resultado esperado** | Validar demanda por simplicidade; aprender sobre o fluxo Kanban. |
| **Métricas** | Ativação, engajamento, conclusão, retenção, NPS. |
| **Custo & Cronograma** | 5 pessoas · 3 sprints de 2 semanas (~6 semanas). |
