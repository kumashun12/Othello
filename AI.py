import random
import field
import player
import copy

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
            best_moves = [(r, c)]
        elif score == best_score:
            best_moves.append((r, c))

    return random.choice(best_moves)

def apply_move(board, r, c, color):
    new_board = copy.deepcopy(board)
    flips = field.get_flips(new_board, r, c, color)
    new_board[r][c] = color
    for fr, fc in flips:
        new_board[fr][fc] = color
    return new_board


def evaluate(board, color):
    black_num = field.black_count(board)
    white_num = field.white_count(board)

    if color == field.BLACK:
        return black_num - white_num
    elif color == field.WHITE:
        return white_num - black_num


def evaluate_weights(board, color):
    total = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == color:
                total += WEIGHTS[r][c] 
            elif board[r][c] == -color:
                total -= WEIGHTS[r][c]

    return total

def one_step_ai(board, color):
    best_score = float('-inf')
    best_moves = []
    for r, c in field.legal_moves(board, color):
        new_board = apply_move(board, r, c, color)
        score = evaluate(new_board, color)
        if score > best_score:
            best_score = score
            best_moves = [(r, c)]
        elif score == best_score:
            best_moves.append((r, c))

    return random.choice(best_moves)


def two_step_ai(board, color):
    my_best_score = float('-inf')
    my_best_moves = []
    for r1, c1 in field.legal_moves(board, color):
        my_board = apply_move(board,r1, c1, color)
        my_score = evaluate(my_board, color)

        moves = field.legal_moves(my_board, -color)
        if moves:
            enemy_worst_score = float('inf')
            for r2, c2 in moves:
                enemy_board = apply_move(my_board, r2, c2, -color)
                enemy_score = evaluate(enemy_board, color)
                if enemy_score < enemy_worst_score:
                    enemy_worst_score = enemy_score

            best_score = enemy_worst_score
        else:
            best_score = my_score


        if best_score > my_best_score:
            my_best_score = best_score
            my_best_moves = [(r1, c1)]
        elif best_score == my_best_score:
            my_best_moves.append((r1, c1))

    return random.choice(my_best_moves)


def one_step_evaluation_ai(board, color):
    best_score = float('-inf')
    best_moves = []
    for r, c in field.legal_moves(board, color):
        new_board = apply_move(board, r, c, color)
        score = evaluate_weights(new_board, color)
        if score > best_score:
            best_score = score
            best_moves = [(r, c)]
        elif score == best_score:
            best_moves.append((r, c))

    return random.choice(best_moves)

        
def two_step_evaluation_ai(board, color):
    my_best_score = float('-inf')
    my_best_moves = []
    for r1, c1 in field.legal_moves(board, color):
        my_board = apply_move(board,r1, c1, color)
        my_score = evaluate_weights(my_board, color)

        moves = field.legal_moves(my_board, -color)
        if moves:
            enemy_worst_score = float('inf')
            for r2, c2 in moves:
                enemy_board = apply_move(my_board, r2, c2, -color)
                enemy_score = evaluate_weights(enemy_board, color)
                if enemy_score < enemy_worst_score:
                    enemy_worst_score = enemy_score

            best_score = enemy_worst_score
        else:
            best_score = my_score


        if best_score > my_best_score:
            my_best_score = best_score
            my_best_moves = [(r1, c1)]
        elif best_score == my_best_score:
            my_best_moves.append((r1, c1))

    return random.choice(my_best_moves)
