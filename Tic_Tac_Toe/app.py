import random

board = [str(i) for i in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")


while True:
    print_board(board)

    move = int(input("Move (0-8): "))
    if board[move] not in ['X', '0']:
        board[move] = 'X'
    else:
        print("Already filled!")
        continue

    while True:
        comp_move = random.randint(0, 8)
        if board[comp_move] not in ['X', '0']:
            board[comp_move] = '0'
            break


    winner_combination = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    def check_winner(board, player):
        for combo in winner_combination:
            if all(board[i] == player for i in combo):
                return True
        return False


    if check_winner(board, 'X'):
        print_board(board)
        print("You win!")
        break

    elif check_winner(board, '0'):
        print_board(board)
        print("computer wins!")
        break

    elif all(cell in ['X', '0'] for cell in board):
        print_board(board)
        print("It's a draw!")
        break
    