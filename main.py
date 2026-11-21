#main.py

import field
import player
import AI
import time

AI_LIST = [AI.random_ai, AI.greedy_algorithm_ai, AI.evaluation_sheet_ai,
           AI.one_step_ai, AI.two_step_ai, AI.one_step_evaluation_ai, AI.two_step_evaluation_ai,
           AI.minimax2_ai, AI.minimax3_ai, AI.minimax4_ai]


#ゲーム開始の流れ
#初期配置⇒先攻（黒）と後攻（白）を決める⇒交互に駒を置いていく

#人間同士で対戦するときの処理（ローカル）

print("対戦するモードを選んでください")
print("1：人 vs 人,  2：人 vs AI,  3：AI vs AI")

game_mode = player.ask_number(1, 3)
players = {field.BLACK: None, field.WHITE: None}

if game_mode == 2:
    print("対戦するAIを選んでください")
    print("1：ランダム, 2：貪欲法, 3：評価表, 4：1手先読み（石の数）, 5：2手先読み（石の数）, 6：1手先読み（位置）, 7：2手先読み（位置）, 8：深さ2, 9：深さ3, 10：深さ4")

    ai_mode = player.ask_number(1, 7)
    players = {field.BLACK: None, field.WHITE: AI_LIST[ai_mode-1]}

elif game_mode == 3:
    print("対戦させるAIを2つ選んでください")
    print("先攻（黒）")
    print("1：ランダム, 2：貪欲法, 3：評価表, 4：1手先読み（石の数）, 5：2手先読み（石の数）, 6：1手先読み（位置）, 7：2手先読み（位置）, 8：深さ2, 9：深さ3, 10：深さ10")
    black_ai_mode = player.ask_number(1, 7)

    print("後攻（白）")
    print("1：ランダム, 2：貪欲法, 3：評価表, 4：1手先読み（石の数）, 5：2手先読み（石の数）, 6：1手先読み（位置）, 7：2手先読み（位置）, 8：深さ2, 9：深さ3, 10：深さ4")
    white_ai_mode = player.ask_number(1, 7)

    players = {field.BLACK: AI_LIST[black_ai_mode-1], field.WHITE: AI_LIST[white_ai_mode-1]}


turn = field.BLACK
board = field.create_board()
print("バトル開始")


#ゲームメイン部分の処理
while True:
    field.print_board(board)

    moves = field.legal_moves(board, turn)

    if not moves:
        if not field.legal_moves(board, -turn):
            break

        print("おける場所がないのでパスします")
        turn *= -1
        continue
    
    print([(r+1, c+1) for r, c in moves])
    if turn == 1:
        print("黒のターンです")
    elif turn == -1:
        print("白のターンです")
    mover = players[turn]

    if mover is None:
        r, c = player.read_input()
    else:
        r, c = mover(board, turn)
        print(f"AIは{r+1, c+1}に置きました")
        time.sleep(3)

    if player.piece(board, r, c, turn):
        turn *= -1
        print("駒を置きました")

#ゲーム終了後の処理
field.game_result(board)



