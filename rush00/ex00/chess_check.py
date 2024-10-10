def is_king_in_check(board):
    if not isinstance(board, list) or not all(isinstance(row, str) and len(row) == len(board) for row in board):
        return "Error: Invalid board structure"

    n = len(board)  
    if n < 1:
        return "Error: Board is too small"

    king_position = None

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if king_position is None:
        return "Error: No King on the board"

    king_x, king_y = king_position

    
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),  
        (1, 1), (1, -1), (-1, 1), (-1, -1)  
    ]

    
    for dx, dy in directions:
        x, y = king_x, king_y
        while 0 <= x < n and 0 <= y < n:
            x += dx
            y += dy
            if 0 <= x < n and 0 <= y < n:
                piece = board[x][y]
                if piece == 'K':  
                    continue
                if piece in 'QRB':  
                    print("Success")
                    return
                if piece != '.': 
                    break

    
    pawn_positions = [(king_x + 1, king_y - 1), (king_x + 1, king_y + 1)]
    for px, py in pawn_positions:
        if 0 <= px < n and 0 <= py < n and board[px][py] == 'P':
            print("Success")
            return

    print("Fail")

board = [
    "........",
    "........",
    "...K....",
    "........",
    "P.......",
    "........",
    ".R......",
    "........"
]
is_king_in_check(board)

board_no_king = [
    "........",
    "........",
    "........",
    ".....K..",
    "P....P..",
    ".....R..",
    ".R......",
    "........"
]
print(is_king_in_check(board_no_king))  
