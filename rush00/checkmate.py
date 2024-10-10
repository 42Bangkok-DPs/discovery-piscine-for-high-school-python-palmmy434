def checkmate(board):
    # Parse the board into a 2D list
    board = [list(row) for row in board.strip().split('\n')]
    n = len(board)  # Size of the board
    king_pos = None

    # Find the King's position
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")  # King not found, this is unexpected behavior
        return

    king_x, king_y = king_pos

    # Directions: (dy, dx) for vertical, horizontal, and diagonal checks
    directions = [
        (1, 0),   # Down
        (-1, 0),  # Up
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 1),   # Down-right
        (1, -1),  # Down-left
        (-1, 1),  # Up-right
        (-1, -1)  # Up-left
    ]

    # Check each direction for threats
    for dy, dx in directions:
        x, y = king_x, king_y
        while 0 <= x < n and 0 <= y < n:
            x += dy
            y += dx
            if 0 <= x < n and 0 <= y < n:
                piece = board[x][y]
                if piece != '.':
                    if piece in 'RQB':  # Rook, Queen, Bishop can attack
                        print("Success")
                        return
                    break  # Any piece other than Rook, Queen, or Bishop stops the check

    # Check for Pawns specifically (they can only attack diagonally)
    for dx in [-1, 1]:  # Left and Right diagonals
        x = king_x + 1  # Pawns can only attack from below (down)
        y = king_y + dx
        if 0 <= x < n and 0 <= y < n:
            if board[x][y] == 'P':
                print("Success")
                return

    print("Fail")
