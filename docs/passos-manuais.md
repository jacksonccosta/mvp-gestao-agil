# Passos manuais para concluir a entrega

Tudo que pode ser produzido localmente já está pronto neste repositório. Os passos
abaixo dependem das **suas contas pessoais** (Miro, Jira, Figma, GitHub, gravação de
vídeo) e precisam ser executados por você. O conteúdo necessário já está todo gerado —
é só transpor/publicar.

---

## 1. Miro — Lean Inception + MVP Canvas (3,0 pts)
1. Acesse https://miro.com/miroverse/lean-inception-workshop/ e **faça uma cópia** do template.
2. Preencha cada etapa usando o conteúdo de [`docs/lean-inception.md`](lean-inception.md).
3. No bloco do MVP Canvas, use o conteúdo de [`docs/mvp-canvas.md`](mvp-canvas.md).
   - Atalho: você pode **arrastar a imagem** [`assets/mvp-canvas.png`](../assets/mvp-canvas.png)
     direto para o board como referência e/ou recriar os post-its.
4. Deixe o board **público** (Share → Anyone with the link → Can view).
5. Teste a URL em uma aba anônima e cole-a em [`canvas-url.txt`](../canvas-url.txt).

## 2. Jira — Backlog do Produto + Sprint (1,5 + 1,5 pts)
1. Crie um projeto (tipo *Scrum*) no Jira.
2. **Importe** o arquivo [`jira-import/jira-backlog-import.csv`](../jira-import/jira-backlog-import.csv):
   - Settings → System → External System Import → CSV.
   - Mapeie as colunas: *Issue Type, Summary, Epic Name, Epic Link, Story Points,
     Priority, Labels, Sprint, Description* e o campo de *Acceptance Criteria*
     (ou concatene em Description, se o campo não existir).
3. Confira épicos, histórias, enablers e o RNF.
4. Os PDFs [`product-backlog.pdf`](../product-backlog.pdf) e
   [`sprint-backlog.pdf`](../sprint-backlog.pdf) **já estão prontos** e refletem o mesmo
   conteúdo — caso prefira, eles atendem ao requisito de "versão legível em PDF".
   Se quiser regerá-los a partir do Jira, exporte e ajuste, mas não é obrigatório.

## 3. Figma — Wireframes (2,0 pts)
- As imagens dos protótipos já estão em [`wireframes/`](../wireframes/) (5 telas da Sprint 1).
- Elas atendem ao requisito ("salve os arquivos Figma como imagens" → imagens na pasta
  `wireframes/`).
- **Opcional / recomendado:** recrie/refine no Figma para ter o arquivo-fonte e reexporte
  por cima destas imagens, mantendo os mesmos nomes.

## 4. Vídeo (2,0 pts)
- Siga o [`docs/video-roteiro.md`](video-roteiro.md).
- Salve como `apresentacao-mvp.mp4` na raiz **ou** crie `video-url.txt` com a URL pública.

## 5. GitHub — publicar o repositório
```bash
cd mvp-gestao-agil
git init
git add .
git commit -m "Entrega MVP — Gestão Ágil de Projetos e Produtos"
git branch -M main
git remote add origin https://github.com/jacksonccosta/mvp-gestao-agil.git
git push -u origin main
```
1. Crie o repositório **público** em https://github.com/new (nome sugerido: `mvp-gestao-agil`).
2. Faça o push (comandos acima).
3. Teste o acesso à URL em uma aba anônima antes de postar a entrega.

---

### Checklist final de entrega
- [ ] `canvas-url.txt` com a URL pública do Miro (testada)
- [ ] `product-backlog.pdf` legível na raiz
- [ ] `sprint-backlog.pdf` legível na raiz
- [ ] Pasta `wireframes/` com as imagens
- [ ] Vídeo (`apresentacao-mvp.mp4`) ou `video-url.txt` na raiz
- [ ] Repositório público no GitHub e URL testada
