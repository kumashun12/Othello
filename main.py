#main.py

import field
import player
import AI
import time

AI_LIST = [AI.random_ai, AI.greedy_algorithm_ai, AI.evaluation_sheet_ai]

#ゲーム開始の流れ
#初期配置⇒先攻（黒）と後攻（白）を決める⇒交互に駒を置いていく

#人間同士で対戦するときの処理（ローカル）

print("対戦するモードを選んでください")
print("1：人 vs 人,  2：人 vs AI,  3：AI vs AI")

while True:
    n = int(input())
    if 1 <= n <= 3:
        battle_mode = n
        break
    else:
        print("1~3で選んでください")

if n == 2:
    print("対戦するAIを選んでください")
    print("1：ランダム, 2：貪欲法, 3：評価表")

    while True:
        n = int(input())
        if 1 <= n <= 3:
            opponent = n
            break
        else:
            print("1~3で選んでください")

elif n == 3:
    print("対戦させるAIを2つ選んでください")
    print("先攻（黒）")
    print("1：ランダム, 2：貪欲法, 3：評価表")
    while True:
        n = int(input())
        if 1 <= n <= 3:
            black_ai = AI_LIST[n-1]
            break
        else:
            print("1~3で選んでください")

    print("後攻（白）")
    print("1：ランダム, 2：貪欲法, 3：評価表")
    while True:
        n = int(input())
        if 1 <= n <= 3:
            white_ai = AI_LIST[n-1]
            break
        else:
            print("1~3で選んでください")

turn = field.BLACK
board = field.create_board()
print("バトル開始")


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
    if battle_mode == 1:
        r, c = player.read_input()
        if player.piece(board, r, c, turn):
            turn *= -1
            print("駒を置きました")

    #人vsAI
    elif battle_mode == 2:
        if turn == field.BLACK:
            r, c = player.read_input()
            time.sleep(1)
        elif turn == field.WHITE:
            #ランダム
            if opponent == 1:
                r, c = AI.random_ai(board, turn)

            #貪欲法
            elif opponent == 2:
                r, c = AI.greedy_algorithm_ai(board, turn)

            #評価表AI
            else:
                r, c = AI.evaluation_sheet_ai(board, turn)
            
            print(f"AIは{r+1, c+1}に置きました")
            time.sleep(3)


        if player.piece(board, r, c, turn):
            turn *= -1
            print("駒を置きました")

    #AIvsAI
    else:
        if turn == field.BLACK:
            r, c = black_ai(board, turn)
        elif turn == field.WHITE:
            r, c = white_ai(board, turn)


        #ランダム
        #r, c = AI.random_ai(board, turn)

        #貪欲法
        #r, c = AI.greedy_algorithm_ai(board, turn)

        #評価表AI
        #r, c = AI.evaluation_sheet_ai(board, turn)

        print(f"AIは{r+1, c+1}に置きました")
        if player.piece(board, r, c, turn):
            turn *= -1
            print("駒を置きました")
        time.sleep(3)

#ゲーム終了後の処理
field.game_result(board)



