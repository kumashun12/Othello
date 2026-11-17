import field

def piece(board, r, c, player):
    
    #すでに駒がおかれているところにはおけないようにする
    if(board[r][c] != field.EMPTY):
        print("そのマスには駒がおかれています")
    else:
        #駒を置く
        print("駒を置きました")
        board[r][c] = player


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

board = field.create_board()

s = read_input()
piece(board, s[0], s[1], field.BLACK)

field.print_board(board)