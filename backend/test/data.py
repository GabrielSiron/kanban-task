from datetime import datetime

TAGS = [
    {
        'title': 'Muito Importante',
        'color': '#FCA321'
    },
    {
        'title': 'Importante',
        'color': '#EEE432'
    },
    {
        'title': 'Normal',
        'color': '#ACA142'
    },
    {
        'title': 'Não prioritário',
        'color': '#5664AC'
    }
]
USERS = [
    {
        'name': 'Gabriel',
        'email': 'gabriel@gmail.com',
        'password': 'Password1!', # TODO Implement bycript
    },
    {
        'name': 'Roberto',
        'email': 'roberto@gmail.com',
        'password': 'Password1!', # TODO Implement bycript
    },
    {
        'name': 'Marcone',
        'email': 'marcone@gmail.com',
        'password': 'Password1!', # TODO Implement bycript
    }
]
    
CYCLES = [
    {
        'limit_date': datetime(2024, 6, 19),
        'title': 'Primeira Semana',
        'user_id': 1
    },
    {
        'limit_date': datetime(2024, 6, 19),
        'title': 'Primeira Semana',
        'user_id': 2
    },
    {
        'limit_date': datetime(2024, 6, 19),
        'title': 'Primeira Semana',
        'user_id': 3
    },
]

DAYS = [
    {
        'date': datetime(2024, 2, 1),
        'cycle_id': 1
    },
    {
        'date': datetime(2024, 2, 2),
        'cycle_id': 1
    },
    {
        'date': datetime(2024, 2, 3),
        'cycle_id': 1
    },
    {
        'date': datetime(2024, 2, 1),
        'cycle_id': 2
    },
    {
        'date': datetime(2024, 2, 2),
        'cycle_id': 2
    },
    {
        'date': datetime(2024, 2, 3),
        'cycle_id': 2
    },
    {
        'date': datetime(2024, 2, 1),
        'cycle_id': 3
    },
    {
        'date': datetime(2024, 2, 2),
        'cycle_id': 3
    },
    {
        'date': datetime(2024, 2, 3),
        'cycle_id': 3
    }
]

TASKS = [
    {
        'title': 'Lavar os Pratos',
        'description': '',
        'tag_id': 1,
        'day_id': 1
    }
]