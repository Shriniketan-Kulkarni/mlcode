#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function to check if a player has won the game
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

# Function to check if the board is full
def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Depth First Search (DFS) function to explore all possible moves
def dfs(board, depth, is_maximizing_player, alpha, beta):
    if check_winner(board, 'X'):
        return -10 + depth
    if check_winner(board, 'O'):
        return 10 - depth
    if is_full(board):
        return 0

    if is_maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # Player O's move
                    eval = dfs(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '  # Undo the move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Player X's move
                    eval = dfs(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '  # Undo the move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI (O)
def find_best_move(board):
    best_move = None
    best_val = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # AI plays 'O'
                move_val = dfs(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '  # Undo the move

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Empty 3x3 board
    print("Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        # Player X (human)
        print("Player X's turn")
        x_move = input("Enter row and column (0-2, space-separated): ").split()
        x_row, x_col = int(x_move[0]), int(x_move[1])

        if board[x_row][x_col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[x_row][x_col] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("Player X wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Player O (AI)
        print("Player O's turn (AI)")
        o_move = find_best_move(board)
        if o_move:
            board[o_move[0]][o_move[1]] = 'O'
            print(f"AI moves at {o_move[0]} {o_move[1]}")
            print_board(board)

            if check_winner(board, 'O'):
                print("Player O (AI) wins!")
                break
            if is_full(board):
                print("It's a draw!")
                break

# Run the game
if __name__ == "__main__":
    play_game()


# In[ ]:




