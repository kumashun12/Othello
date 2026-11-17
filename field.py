

EMPTY = 0
BLACK = 1
WHITE = -1

STONE_MAP = {
        EMPTY: "*",
        WHITE: "○",
        BLACK: "●",
    }


def create_board():
    board = [[EMPTY for j in range(8)] for i in range(8)]

    #オセロの初期配置を決めるためにしろと黒の駒を表現
    board[3][3] = WHITE
    board[4][4] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK

    return board


def print_board(board):
    #x軸を表示
    print("  1 2 3 4 5 6 7 8")
    for r in range(8):
        print(r + 1, end=" ")
        for c in range(8):
            print(STONE_MAP[board[r][c]], end=" ")
        print()

board = create_board()
print_board(board)

