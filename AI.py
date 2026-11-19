import random
import math
import field

#ランダムAI
def random_ai(board, color):
    choice = random.choice(field.legal_moves(board, color))
    return choice


#貪欲法AI
def greedy_algorithm_ai(board, color):
    moves = field.legal_moves(board, color)
    best_move = None
    best_count = -1
    for r, c in moves:
        num = len(field.get_flips(board, r, c, color))
        if num > best_count:
            best_count = num
            best_move = (r, c)

    return best_move