#player.py

import field

def piece(board, r, c, player):

    #すでに駒がおかれているところにはおけないようにする
    if(board[r][c] != field.EMPTY):
        print("そのマスには駒がおかれています")
        return False
    else:
        #駒を置く
        if field.is_adjacent(board, r, c):
            print("駒を置きました")
            board[r][c] = player
            return True
        else:
            print("駒の隣においてください")
            return False


def read_input():

    print("1~8の間で数字を2つ入力してください")
    print("例：1 2")

    while True:
        try:
            r, c = map(int, input().split())
            if(1 <= r <= 8 and 1 <= c <= 8):
                return r-1, c-1
            else:
                print("1~8の間の数字で入力してください")

        except ValueError:
            print("入力が不正です。もう一度入力してください")
