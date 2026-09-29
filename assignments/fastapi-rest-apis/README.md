# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST em Python usando o framework FastAPI, definindo rotas, modelos de dados, operações CRUD e respostas HTTP apropriadas.

## 📝 Tarefas

### 🛠️ Criar a Aplicação FastAPI

#### Descrição

Configure uma aplicação FastAPI e crie uma rota inicial para confirmar que a API está funcionando.

#### Requisitos

O programa concluído deve:

- Criar uma instância de `FastAPI`.
- Disponibilizar uma rota `GET /` que retorne uma mensagem de status em JSON.
- Permitir que a aplicação seja executada com um servidor ASGI, como o Uvicorn.
- Disponibilizar a documentação interativa nos caminhos padrão `/docs` ou `/redoc`.

### 🛠️ Implementar Operações CRUD

#### Descrição

Modele um recurso de tarefas e implemente endpoints para criar, consultar, atualizar e remover tarefas armazenadas em memória.

#### Requisitos

O programa concluído deve:

- Definir um modelo Pydantic com os dados necessários para uma tarefa.
- Implementar endpoints `POST`, `GET`, `PUT` ou `PATCH` e `DELETE` para o recurso.
- Retornar o recurso criado ou atualizado em formato JSON.
- Retornar uma lista de tarefas quando o cliente consultar a coleção.
- Usar identificadores únicos para localizar tarefas individuais.

### 🛠️ Validar Dados e Tratar Erros

#### Descrição

Melhore a API para validar as entradas recebidas e informar corretamente os clientes quando uma tarefa não puder ser encontrada ou processada.

#### Requisitos

O programa concluído deve:

- Rejeitar dados inválidos usando validação do Pydantic.
- Retornar o status HTTP `404` quando uma tarefa solicitada não existir.
- Usar códigos de status HTTP coerentes para criação, sucesso e remoção de recursos.
- Permitir que o cliente filtre ou consulte tarefas conforme um critério definido pela aplicação.
- Demonstrar pelo menos uma chamada à API usando a documentação interativa ou um cliente HTTP.
