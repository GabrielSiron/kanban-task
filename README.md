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
-$ python -m venv env
-$ env/Scripts/activate
(env) -$ pip install -r requirements.txt
(env) -$ pre-commit install
```

Isso fará com que todos os seus commits passem por uma reformatação, utilizando a biblioteca black. Outras bibliotecas, com outros objetivos, podem ser adicionadas a ferramenta de pre-commit. 

As dependências já estarão instaladas no container, mas é necessário criar um virtual environment externo porque o git executa fora do container, e o pre-commit precisa das dependências listadas no requirements.txt.