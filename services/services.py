from lexicon import LEXICON_RU

def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if user_answer == LEXICON_RU[key]:
            return key

def get_result(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {'stone': 'scissors',
             'scissors': 'paper',
             'paper': 'stone'}
    if user_choice == bot_choice:
        return 'draw'
    elif rules[user_choice] == bot_choice:
        return 'win'
    return 'lose'
