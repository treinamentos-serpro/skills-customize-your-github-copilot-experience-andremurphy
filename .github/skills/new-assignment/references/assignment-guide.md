# Guia para Novas Tarefas

Use este guia ao criar uma nova tarefa de programação para os alunos.

## Escopo e Dificuldade

- Escolha um único conceito ou um conjunto pequeno de conceitos relacionados.
- Defina um objetivo que possa ser concluído em uma sessão de estudo.
- Organize os requisitos do mais simples ao mais elaborado.
- Especifique resultados observáveis e evite requisitos vagos.
- Use linguagem adequada ao nível da turma e explique termos essenciais.

## Estrutura da Tarefa

Crie a tarefa em `assignments/<id>/` e use o [template de assignment](../../../templates/assignment-template.md) para o `README.md`.

O README deve conter:

- `# 📘 Atividade: [Título da Atividade]`
- `## 🎯 Objetivo`
- `## 📝 Tarefas`
- Uma ou mais tarefas com `Descrição` e `Requisitos`.

Não inclua seções extras sem uma necessidade clara para a atividade.

## Starter Code e Dados

Inclua arquivos adicionais somente quando ajudarem o aluno a começar ou quando forem parte essencial do exercício:

- Use `starter-code.py` para fornecer uma estrutura inicial ou pontos de extensão.
- Use `data.csv` quando a tarefa exigir um conjunto de dados fornecido pelo projeto.
- Mantenha os arquivos iniciais mínimos e coerentes com os requisitos do README.
- Não inclua a solução completa no starter code.

## Requisitos de Qualidade

Cada requisito deve ser implementável e verificável. Quando fizer sentido, inclua exemplos de entrada e saída em blocos de código. Mantenha nomes de arquivos, identificadores e instruções consistentes entre o README e os arquivos da tarefa.

## Checklist

Antes de concluir uma nova tarefa:

- A pasta usa um identificador curto em kebab-case.
- O arquivo principal se chama `README.md`.
- O README segue o template do projeto.
- O objetivo descreve claramente o aprendizado esperado.
- Os requisitos são específicos e mensuráveis.
- Os arquivos opcionais são necessários e não contêm a solução.
- A tarefa foi registrada no `config.json` quando for exibida no site.
- Os arquivos criados foram validados e estão no diretório correto.

# Assignment Design Guide

Orientações para desenhar conteúdo de assignment: o que ensinar e como definir o escopo. Para formatação e estrutura em markdown, os arquivos de instruções do projeto já tratam isso automaticamente.

## Difficulty & Scope

- Defina de 2 a 4 tarefas por assignment que evoluam entre si
- Comece com algo que um aluno consiga terminar em menos de 10 minutos e depois aumente a complexidade
- A última tarefa pode ser um objetivo ambicioso, mas as anteriores devem construir confiança
- Foque em um conceito central por assignment (ex.: "loops", não "loops + file I/O + error handling")

## Starter Code

Inclua starter code quando:

- A assignment precisar de boilerplate que o estudante não deve escrever do zero
- Você quiser que os estudantes sigam uma assinatura de função ou estrutura específica

Evite quando o objetivo for escrever algo do zero (ex.: "write a script that...").

## Exemplos de Tópicos por Dificuldade

- **Beginner**: variables, conditionals, loops, string formatting
- **Intermediate**: functions, lists/dicts, file I/O, basic classes
- **Advanced**: APIs, data analysis, testing, web frameworks