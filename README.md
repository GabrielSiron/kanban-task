# kanban-task

## Como Rodar o Projeto - Python

1. Buildar a aplicação:
```
-$ docker network create backend
-$ docker volume create db-volume
-$ docker-compose build
```

2. Rodar a aplicação
```
-$ docker-compose up
```

Se algum dos serviços não for necessário num dado momento, execute 

```
-$ docker-compose up [service-name]
```
indicando o nome do serviço que você de fato fará uso.

### Detalhes

é possível configurar uma ferramenta de pre-commit na aplicação Python. Para isso, faça
```
-$ cd backend/
-$ python -m venv env
-$ env/Scripts/activate
(env) -$ pip install -r pre-commit-requirements.txt
(env) -$ pre-commit install
```

Isso fará com que todos os seus commits passem por uma reformatação, utilizando a biblioteca black. Outras bibliotecas, com outros objetivos, podem ser adicionadas a ferramenta de pre-commit. 

OBS: nenhuma dependência do projeto é necessária ao pre-commit, por isso temos um arquivo só para as dependências dele.