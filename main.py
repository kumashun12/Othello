#main.py

import field
import player
import AI
import time

#ゲーム開始の流れ
#初期配置⇒先攻（黒）と後攻（白）を決める⇒交互に駒を置いていく

#人間同士で対戦するときの処理（ローカル）
turn = field.BLACK
print("先攻は黒です")
board = field.create_board()



#ゲームメイン部分の処理
while True:
    field.print_board(board)

    moves = field.legal_moves(board, turn)
    if turn == 1:
        print("黒のターンです")
    elif turn == -1:
        print("白のターンです")

    if not moves:
        if not field.legal_moves(board, -turn):
            break

        print("おける場所がないのでパスします")
        turn *= -1
        continue

    print([(r+1, c+1) for r, c in moves])

    #人vs人
    """
    r, c = player.read_input()
    if player.piece(board, r, c, turn):
        turn *= -1
    """

    #人vsAI
    """
    if turn == field.BLACK:
        r, c = player.read_input()
        time.sleep(1)
    elif turn == field.WHITE:
        #ランダム
        #r, c = AI.random_ai(board, turn)

        #貪欲法
        r, c = AI.greedy_algorithm_ai(board, turn)

        #評価表AI
        r, c = AI.evaluation_sheet_ai(board, turn)
        print(f"AIは{r+1, c+1}に置きました")
        time.sleep(3)


    if player.piece(board, r, c, turn):
        turn *= -1
    """

    #AIvsAI
    #ランダム
    #r, c = AI.random_ai(board, turn)

    #貪欲法
    #r, c = AI.greedy_algorithm_ai(board, turn)

    #評価表AI
    r, c = AI.evaluation_sheet_ai(board, turn)

    print(f"AIは{r+1, c+1}に置きました")
    if player.piece(board, r, c, turn):
        turn *= -1
    time.sleep(3)

#ゲーム終了後の処理
field.game_result(board)



