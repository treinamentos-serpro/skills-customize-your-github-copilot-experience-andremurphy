---
name: new-assignment
description: "Use when creating a new programming assignment in assignments/, including its README.md and optional starter files."
---

# Criar Nova Tarefa

Use este fluxo para criar uma nova tarefa educacional no diretório `assignments/`.

## Estrutura

1. Crie uma pasta com um identificador curto e descritivo em `assignments/<id-da-tarefa>/`.
2. Crie o arquivo obrigatório `assignments/<id-da-tarefa>/README.md`.
3. Adicione arquivos opcionais, como `starter-code.py` ou `data.csv`, somente quando forem necessários para a tarefa.

## README.md

Siga exatamente o template [`templates/assignment-template.md`](../../../templates/assignment-template.md):

- Use o título `# 📘 Atividade: [Título da Atividade]`.
- Inclua `## 🎯 Objetivo` com 1 ou 2 frases sobre o aprendizado esperado.
- Inclua `## 📝 Tarefas`.
- Para cada tarefa, use `### 🛠️ [Título da Tarefa]`.
- Inclua `#### Descrição` com instruções claras para o aluno.
- Inclua `#### Requisitos` com resultados específicos e mensuráveis em bullet points.
- Não inclua seções extras sem necessidade.

## Conteúdo Educacional

- Use linguagem clara e adequada ao nível da turma.
- Defina objetivos de aprendizagem concretos.
- Mantenha os requisitos coerentes com os arquivos iniciais fornecidos.
- Inclua exemplos de entrada e saída em blocos de código quando ajudarem na compreensão.

## Validação

Antes de concluir:

- Confirme que o arquivo principal se chama `README.md`.
- Verifique se todos os cabeçalhos obrigatórios estão presentes.
- Confirme que os requisitos são implementáveis e verificáveis.
- Execute a validação disponível para o tipo de arquivo criado.

---
name: new-assignment
description: Crie uma nova assignment de programação para estudantes da Mergington High School. Use esta skill sempre que o usuário quiser criar, adicionar, estruturar ou gerar uma nova assignment, exercício ou homework, mesmo que não use explicitamente a palavra "assignment".
---

# Criar Nova Tarefa de Programação

As assignments ficam em `assignments/<id>/`, e o site lê `config.json` para exibi-las. Siga estas etapas para criar ambos.

## Etapa 1: Coletar Requisitos

Se o usuário não tiver especificado, pergunte qual conceito de programação a assignment deve abordar.

> 📖 Leia [references/assignment-guide.md](references/assignment-guide.md) para orientações sobre dificuldade, escopo e quando incluir starter code.

## Etapa 2: Criar a Assignment

1. Crie `assignments/<kebab-case-id>/README.md` seguindo o [assignment template](../../../templates/assignment-template.md)
2. (Opcional) Adicione starter code ou arquivos de dados no mesmo diretório

## Etapa 3: Registrar no Website

Use os scripts incluídos; NÃO edite `config.json` manualmente.

**Registrar a assignment:**

    node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"

**Registrar cada arquivo como attachment** (starter code, arquivos de dados etc.):

    node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>

Tipos comuns: `python`, `csv`, `json`, `txt`, `html`

## Etapa 4: Verificar

Confirme que a assignment foi registrada corretamente: verifique se `config.json` contém a nova entrada e se todos os arquivos criados existem no disco.