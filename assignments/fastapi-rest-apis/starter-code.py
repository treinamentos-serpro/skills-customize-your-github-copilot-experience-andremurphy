from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Tasks API")


class Task(BaseModel):
    title: str
    completed: bool = False


# Armazenamento temporário em memória para a atividade.
tasks: dict[int, Task] = {}
next_id = 1


@app.get("/")
def read_root():
    return {"message": "Tasks API is running"}


# TODO: Crie um endpoint POST /tasks para adicionar uma tarefa.
# TODO: Crie um endpoint GET /tasks para listar todas as tarefas.
# TODO: Crie um endpoint GET /tasks/{task_id} para buscar uma tarefa.
# TODO: Crie um endpoint PUT ou PATCH /tasks/{task_id} para atualizar uma tarefa.
# TODO: Crie um endpoint DELETE /tasks/{task_id} para remover uma tarefa.
# TODO: Adicione validação e respostas HTTP apropriadas para tarefas inexistentes.
