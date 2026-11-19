import random
import field
              
WEIGHTS = [[100, -20, 10,  5,  5, 10, -20, 100],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [ 10,  -2, -1, -1, -1, -1,  -2,  10],
            [  5,  -2, -1, -1, -1, -1,  -2,   5],
            [  5,  -2, -1, -1, -1, -1,  -2,   5],
            [ 10,  -2, -1, -1, -1, -1,  -2,  10],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [100, -20, 10,  5,  5, 10, -20, 100],
           ]     
#WEIGHTSをこう書くことで8*8マスで
#オセロのそれぞれのマス点数で評価したリストを用意してくれる

#ランダムAI
def random_ai(board, color):
    choice = random.choice(field.legal_moves(board, color))
    return choice


#貪欲法AI
def greedy_algorithm_ai(board, color):
    moves = field.legal_moves(board, color)
    best_moves = []
    best_count = -1
    for r, c in moves:
        num = len(field.get_flips(board, r, c, color))
        if num > best_count:
            best_count = num
            best_moves = []
            best_moves.append((r, c))
        elif num == best_count:
            best_moves.append((r, c))

    return random.choice(best_moves)


#評価表AI
def evaluation_sheet_ai(board, color):
    best_moves = []
    moves = field.legal_moves(board, color)
    best_score = float('-inf')
    for r, c in moves:
        score = WEIGHTS[r][c]
        if  score > best_score:
            best_score = score
            best_moves = []
            best_moves.append((r, c))
        elif score == best_score:
            best_moves.append((r, c))

    return random.choice(best_moves)