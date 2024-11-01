from aiogram.types import Message

users: dict[int, dict] = {}


def get_score(message: Message, reset: bool = False, result: str = None) -> str:
    user = message.from_user
    if user.id not in users or reset:
        users[user.id] = {
            'name': user.first_name,
            'win': 0,
            'lose': 0,
            'draw': 0
        }
    if result:
        users[user.id][result] += 1
    return f'''<b>СЧЕТ</b>\n
{users[user.id]["name"]} - {users[user.id]["win"]}
БОТ - {users[user.id]["lose"]}
Ничья - {users[user.id]["draw"]}'''
