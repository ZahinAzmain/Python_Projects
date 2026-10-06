#Tic-Tac-Toe Game

def print_board(board):
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board):
    win_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in win_lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return " " not in board


def get_move(player, board):
    while True:
        choice = input(f"Player {player}, enter your move (1-9): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Please enter a number between 1 and 9.")
            continue
        pos = int(choice) - 1
        if board[pos] != " ":
            print("That square is already taken. Try again.")
            continue
        return pos


def main():
    board = [" "] * 9
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9, left to right, top to bottom:")
    print_board([str(i) for i in range(1, 10)])

    while True:
        current_player = players[turn % 2]
        print_board(board)
        pos = get_move(current_player, board)
        board[pos] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1

    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()