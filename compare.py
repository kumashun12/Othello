import player
import field
import AI

NUM = 100

def game_result(stage):
        black_result = field.black_count(stage)
        white_result = field.white_count(stage)
        if black_result > white_result:
            return field.BLACK
        elif black_result < white_result:
            return field.WHITE
        else:
            return field.EMPTY
        

def repeat(func1, func2, num):
    black_wins = 0
    white_wins = 0
    draw = 0

    for i in range(num):
        turn = field.BLACK
        board = field.create_board()
        while True:
            moves = field.legal_moves(board, turn)

            if not moves:
                if not field.legal_moves(board, -turn):
                    break

                turn *= -1
                continue

            if turn == field.BLACK:
                r, c = func1(board, turn)
            elif turn == field.WHITE:
                r, c = func2(board, turn)

            if player.piece(board, r, c, turn):
                turn *= -1

        winner = game_result(board)

        if (winner == field.BLACK):
            black_wins += 1 
        elif (winner == field.WHITE):
            white_wins += 1
        else:
            draw += 1
        

    black_win_rate = black_wins/num
    white_win_rate = white_wins/num
    draw_rate = draw/num
    return black_win_rate, white_win_rate, draw_rate

"""
black_rate, white_rate, draw_rate = repeat(AI.random_ai, AI.greedy_algorithm_ai, NUM)
print(f"ランダム （黒）対 貪欲法   （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.greedy_algorithm_ai, AI.random_ai, NUM)
print(f"貪欲法   （黒）対 ランダム （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.random_ai, AI.evaluation_sheet_ai, NUM)
print(f"ランダム （黒）対 評価表   （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.random_ai, NUM)
print(f"評価表   （黒）対 ランダム （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.greedy_algorithm_ai, AI.evaluation_sheet_ai, NUM)
print(f"貪欲法   （黒）対 評価表   （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.greedy_algorithm_ai, NUM)
print(f"評価表   （黒）対 貪欲法   （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.two_step_ai, AI.one_step_ai, NUM)
print(f"2手先読み（黒）対 1手先読み（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.one_step_ai, AI.two_step_ai, NUM)
print(f"1手先読み（黒）対 2手先読み（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.two_step_ai, AI.evaluation_sheet_ai, NUM)
print(f"2手先読み（黒）対 評価表   （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.two_step_ai, NUM)
print(f"評価表   （黒）対 2手先読み（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.one_step_ai, AI.evaluation_sheet_ai, NUM)
print(f"1手先読み（黒）対 評価表（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.one_step_ai, NUM)
print(f"評価表   （黒）対 1手先読み（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.two_step_evaluation_ai, AI.one_step_evaluation_ai, NUM)
print(f"2手先読み評価（黒）対 1手先読み評価（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.one_step_evaluation_ai, AI.two_step_evaluation_ai, NUM)
print(f"1手先読み評価（黒）対 2手先読み評価（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.two_step_evaluation_ai, AI.two_step_ai, NUM)
print(f"2手先読み評価   （黒）対 2手先読み（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.two_step_ai, AI.two_step_evaluation_ai, NUM)
print(f"2手先読み   （黒）対 2手先読み評価（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.one_step_evaluation_ai, AI.one_step_ai, NUM)
print(f"1手先読み評価   （黒）対 1手先読み（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.one_step_ai, AI.one_step_evaluation_ai, NUM)
print(f"1手先読み   （黒）対 1手先読み評価（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.two_step_evaluation_ai, AI.evaluation_sheet_ai, NUM)
print(f"2手先読み評価   （黒）対 評価表（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.two_step_evaluation_ai, NUM)
print(f"評価表   （黒）対 2手先読み評価（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.minimax2_ai, AI.two_step_evaluation_ai, NUM)
print(f"深さ2   （黒）対 2手先読み評価（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.minimax3_ai, AI.minimax2_ai, NUM)
print(f"深さ3   （黒）対 深さ2（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.minimax4_ai, AI.minimax3_ai, NUM)
print(f"深さ4   （黒）対 深さ3（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.minimax2_ai, AI.evaluation_sheet_ai, NUM)
print(f"深さ2   （黒）対 評価表（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.minimax3_ai, AI.evaluation_sheet_ai, NUM)
print(f"深さ3   （黒）対 評価表（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.minimax2_ai, NUM)
print(f"評価表   （黒）対 深さ2（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.minimax3_ai, NUM)
print(f"評価表   （黒）対 深さ3（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")
"""

black_rate, white_rate, draw_rate = repeat(AI.minimax4_ai, AI.evaluation_sheet_ai, 100)
print(f"深さ4  （黒）対 評価表（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.minimax4_ai, 100)
print(f"評価表   （黒）対 深さ4（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")