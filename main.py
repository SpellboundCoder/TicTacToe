import logo


def print_board(board):
    print('   A | B | C')
    print("-" * 15)
    row_number = 0
    for row in board:
        row_number += 1
        print(f'{row_number} ', " | ".join(row))
        print("-" * 15)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_full(board):
    return all([cell != ' ' for row in board for cell in row])


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        try:
            choice = input(f"Player {current_player}, enter the column (A, B, C) and row (1, 2, 3): ")
            letter = choice[0].lower()
            abc = ["a", "b", "c"]
            letter_index = abc.index(letter)
            number_index = int(choice[1]) - 1
            if board[number_index][letter_index] != ' ':
                print("Cell already taken, choose another one.")
                continue
        except (ValueError, IndexError):
            print("Invalid input, please enter numbers 0, 1, or 2.")
            continue

        board[number_index][letter_index] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    print(logo.tictactoe)
    print(logo.board)
    tic_tac_toe()
