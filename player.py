#player.py

import field

def piece(board, r, c, turn):

    #すでに駒がおかれているところにはおけないようにする
    if(board[r][c] != field.EMPTY):
        print("そのマスには駒がおかれています")
        return False
    else:
        #駒を置く
        flips = field.get_flips(board, r, c, turn)
        if flips:
            board[r][c] = turn
            
            for fr, fc in flips:
                board[fr][fc] = turn
            return True
        else:
            print("そこにはおけません")
            return False


def read_input():

    print("石を置くときは「行 列」の順に入力します")
    print("（行＝上から何番目、列＝左から何番目）例：3 4")

    while True:
        try:
            r, c = map(int, input().split())
            if(1 <= r <= 8 and 1 <= c <= 8):
                return r-1, c-1
            else:
                print("1~8の間の数字で入力してください")

        except ValueError:
            print("入力が不正です。もう一度入力してください")


def ask_number(low, high):
    while True:
        try:
            n = int(input("整数を入力:"))
            if low <= n <= high:
                return n
            else:
                print(f"{low}~{high}の整数を入力してください")
        except ValueError:
            print(f"{low}~{high}の整数を入力してください")
