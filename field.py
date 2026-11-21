#field.py

EMPTY = 0
BLACK = 1
WHITE = -1

STONE_MAP = {
        EMPTY: "*",
        WHITE: "●",
        BLACK: "○",
}

DIRECTIONS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


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

#隣に駒がおいてるかどうかを調べている
def is_adjacent(board, r, c):
    if board[r][c] != EMPTY:
        return False

    for dr, dc in DIRECTIONS:
        row, col = r + dr, c + dc

        if 0<=row<8 and 0<=col<8:
            if board[row][col] != EMPTY:
                return True

    return False


def get_flips(board, r, c, color):
    flips = []
    for dr, dc in DIRECTIONS:
        row, col = r + dr, c + dc
        candidate = []

        while 0<=row<8 and 0<=col<8:
            if board[row][col] == -color:
                candidate.append((row, col))
            elif board[row][col] == color:
                flips.extend(candidate)
                break
            elif board[row][col] == EMPTY:
                break

            row += dr
            col += dc

    return flips


def legal_moves(board, color):
    coordinate = []
    for r in range(8):
        for c in range(8):
            if board[r][c] == EMPTY and get_flips(board, r, c, color):
                coordinate.append((r, c))

    return coordinate


def white_count(board):
    count = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == WHITE:
                count += 1

    return count


def black_count(board):
    count = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == BLACK:
                count += 1

    return count


def game_result(board):
    black_result = black_count(board)
    white_result = white_count(board)
    print("対戦結果")
    print(f"黒：{black_result} 対 白：{white_result}")
    if black_result > white_result:
        print("黒の勝ち！")
    elif black_result < white_result:
        print("白の勝ち！")
    else:
        print("引き分け") 

        



