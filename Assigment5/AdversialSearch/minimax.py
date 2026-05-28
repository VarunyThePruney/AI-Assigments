from .games.tic_tac_toe import TicTacToe

def minimax(game, depth, maximizing):
    
    if game.winner("X"):
        return 1

    if game.winner("O"):
        return -1

    if game.is_draw():
        return 0

    if maximizing:
        best_score = -float("inf")

        for move in game.available_moves():
            game.make_move(move, "X")

            score = minimax(game, depth + 1, False)

            game.undo_move(move)

            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for move in game.available_moves():
            game.make_move(move, "O")

            score = minimax(game, depth + 1, True)

            game.undo_move(move)

            best_score = min(best_score, score)

        return best_score


def best_move(game):
    best_score = -float("inf")
    move_choice = None

    for move in game.available_moves():
        game.make_move(move, "X")

        score = minimax(game, 0, False)

        game.undo_move(move)

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice


if __name__ == "__main__":

    game = TicTacToe()

    while not game.game_over():

        game.print_board()

        user_move = int(input("Enter position (0-8): "))
        game.make_move(user_move, "O")

        if game.game_over():
            break

        ai_move = best_move(game)
        game.make_move(ai_move, "X")

        print(f"AI chose position {ai_move}")

    game.print_board()

    if game.winner("X"):
        print("AI wins!")

    elif game.winner("O"):
        print("You win!")

    else:
        print("Draw!")