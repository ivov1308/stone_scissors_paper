from aiogram.types import Message

users: dict = {}


def get_user(message: Message):
    user = message.from_user
    if user.id not in users:
        users[user.id] = {
            'name': user.first_name,
            'win': 0,
            'lose': 0,
            'draw': 0
        }
    return users[user.id]

def reset_user(message: Message):
    user = message.from_user
    if user.id in users:
        users[user.id] = {
            'name': user.first_name,
            'win': 0,
            'lose': 0,
            'draw': 0
        }
