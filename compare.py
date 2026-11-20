import player
import field
import AI

def game_result(stage):
        black_result = field.black_count(stage)
        white_result = field.white_count(stage)
        if black_result > white_result:
            return field.BLACK
        elif black_result < white_result:
            return field.WHITE
        else:
            return field.EMPTY
        

def repeat(func1, func2):
    black_wins = 0
    white_wins = 0
    draw = 0

    for i in range(100):
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
        

    black_win_rate = black_wins/100
    white_win_rate = white_wins/100
    draw_rate = draw/100
    return black_win_rate, white_win_rate, draw_rate


black_rate, white_rate, draw_rate = repeat(AI.random_ai, AI.greedy_algorithm_ai)
print(f"ランダム（黒）対 貪欲法  （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.greedy_algorithm_ai, AI.random_ai)
print(f"貪欲法  （黒）対 ランダム（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.random_ai, AI.evaluation_sheet_ai)
print(f"ランダム（黒）対 評価表  （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.random_ai)
print(f"評価表  （黒）対 ランダム（白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.greedy_algorithm_ai, AI.evaluation_sheet_ai)
print(f"貪欲法  （黒）対 評価表  （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")

black_rate, white_rate, draw_rate = repeat(AI.evaluation_sheet_ai, AI.greedy_algorithm_ai)
print(f"評価表  （黒）対 貪欲法  （白）：黒の勝率{black_rate:.0%}、白の勝率{white_rate:.0%}、引き分け{draw_rate:.0%}")