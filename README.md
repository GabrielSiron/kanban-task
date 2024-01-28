# Welcome to the Kanban task

A app for your daily tasks


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

### Testes Unitários

Testes unitários são de suma importância para o desenvolvimento sustentável de uma aplicação. Nossos testes rodam numa base de dados a parte, e devem abranger todos os endpoints que servimos na API.

Na pasta `test`, temos o seguinte esqueleto:

```
| test/
|---- seeder/
|--------- __init__.py # arquivo que popula o database
|---- __init__.py
|---- data.py   # arquivo que alimenta o seeder
|---- user.py   # arquivo de testes dos endpoints de user
```

Cada entidade terá seu próprio arquivo, onde seus testes devem ser implementados.

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

## Contributors
<div style="display:flex; gap: 20px">
<div style="display:flex; flex-direction: column; text-align:center;">

![Marcone Ribeiro](https://avatars.githubusercontent.com/u/41484946?s=200&v=4 "Marcone Ribeiro")<br>
[Marcone Ribeiro](https://github.com/M4RC0N3)

</div>

<div style="display:flex; flex-direction: column; text-align:center;">

![Gabriel Siron](https://avatars.githubusercontent.com/u/56319681?s=200&v=4 "Gabriel Siron")<br>
[Gabriel Siron](https://github.com/GabrielSiron)
</div>
</div>
# kanban-task
