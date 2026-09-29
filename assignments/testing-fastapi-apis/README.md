# 📘 Atividade: Testando APIs Python com pytest

## 🎯 Objetivo

Aprenda a testar automaticamente uma API FastAPI usando pytest e TestClient, verificando respostas, códigos HTTP e comportamentos de sucesso e erro.

## 📝 Tarefas

### 🛠️ Criar Testes de Disponibilidade da API

#### Descrição

Use o `TestClient` do FastAPI para criar testes que confirmem se a API de tarefas está disponível e responde corretamente à rota inicial.

#### Requisitos

O programa concluído deve:

- Configurar o pytest e o `TestClient` para testar a aplicação FastAPI.
- Criar um teste para a rota `GET /`.
- Verificar que a resposta possui status HTTP `200`.
- Verificar que o corpo da resposta contém a mensagem esperada.

### 🛠️ Testar Operações CRUD

#### Descrição

Escreva testes para as operações de criação, consulta, atualização e remoção de tarefas da API desenvolvida na assignment de FastAPI.

#### Requisitos

O programa concluído deve:

- Testar a criação de uma tarefa com `POST` e verificar os dados retornados.
- Testar a consulta da coleção e de uma tarefa individual com `GET`.
- Testar a atualização de uma tarefa com `PUT` ou `PATCH`.
- Testar a remoção de uma tarefa com `DELETE`.
- Verificar os códigos HTTP e os campos principais das respostas em cada operação.

### 🛠️ Cobrir Casos de Erro e Validação

#### Descrição

Amplie a suíte de testes para verificar como a API reage a dados inválidos e a tarefas que não existem.

#### Requisitos

O programa concluído deve:

- Verificar que uma tarefa inexistente retorna status HTTP `404`.
- Verificar que dados inválidos são rejeitados com um status HTTP de erro apropriado.
- Testar pelo menos um caso de corpo de requisição incompleto ou com tipo incorreto.
- Garantir que os testes possam ser executados novamente sem depender da ordem de execução.
- Executar toda a suíte com pytest sem falhas.
