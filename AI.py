def get_moves(board):
    moves = []
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            # Check for horizontal swap
            if j < cols - 1:
                # Swap and check if it forms a valid move
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                if is_valid_move(board):
                    moves.append(((i, j), (i, j+1)))
                # Swap back
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

            # Check for vertical swap
            if i < rows - 1:
                # Swap and check if it forms a valid move
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                if is_valid_move(board):
                    moves.append(((i, j), (i+1, j)))
                # Swap back
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

    return moves

# Currently only checks for three-in-a-row
def is_valid_move(board):
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    # Check rows
    for i in range(rows):
        count = 1
        for j in range(1, cols):
            if board[i][j] == board[i][j-1]:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 1

    # Check columns
    for j in range(cols):
        count = 1
        for i in range(1, rows):
            if board[i][j] == board[i-1][j]:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 1

    return False