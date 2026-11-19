import random
import field
import player

#ランダムAI
def random_ai(board, color):
    choice = random.choice(field.legal_moves(board, color))
    return choice