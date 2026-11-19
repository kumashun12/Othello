#main.py

import field
import player
import random

#ゲーム開始の流れ
#初期配置⇒先攻（黒）と後攻（白）を決める⇒交互に駒を置いていく

"""
#AI戦の時のやつ
human_color = random.randint(0, 1)
if human_color == 1:
    human_color = field.BLACK
    print("先攻は黒です")
else:
    turn = field.WHITE
    print("後攻は白です")
"""

#人間同士で対戦するときの処理（ローカル）
turn = field.BLACK
print("先攻は黒です")
board = field.create_board()



#ゲームメイン部分の処理
while True:
    field.print_board(board)
    if turn == 1:
        print("黒のターンです")
    elif turn == -1:
        print("白のターンです")

    moves = field.legal_moves(board, turn)
    if not moves:
        if not field.legal_moves(board, -turn):
            break

        print("おける場所がないのでパスします")
        turn *= -1
        continue

    print([(r+1, c+1) for r, c in moves])

    r, c = player.read_input()
    if player.piece(board, r, c, turn):
        turn *= -1


#ゲーム終了後の処理
field.game_result(board)



