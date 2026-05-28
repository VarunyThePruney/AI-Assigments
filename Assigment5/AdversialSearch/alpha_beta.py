# alpha_beta.py

from .games.tic_tac_toe import TicTacToe


def alpha_beta(game, depth, alpha, beta, maximizing):

    # Terminal states
    if game.winner("X"):
        return 1

    if game.winner("O"):
        return -1

    if game.is_draw():
        return 0

    # Maximizing player
    if maximizing:

        best_score = -float("inf")

        for move in game.available_moves():

            game.make_move(move, "X")

            score = alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                False
            )

            game.undo_move(move)

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            # Pruning
            if beta <= alpha:
                break

        return best_score

    # Minimizing player
    else:

        best_score = float("inf")

        for move in game.available_moves():

            game.make_move(move, "O")

            score = alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                True
            )

            game.undo_move(move)

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            # Pruning
            if beta <= alpha:
                break

        return best_score


def best_move(game):

    best_score = -float("inf")
    move_choice = None

    alpha = -float("inf")
    beta = float("inf")

    for move in game.available_moves():

        game.make_move(move, "X")

        score = alpha_beta(
            game,
            0,
            alpha,
            beta,
            False
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            move_choice = move

        alpha = max(alpha, best_score)

    return move_choice


if __name__ == "__main__":

    game = TicTacToe()

    print("Tic Tac Toe - Alpha Beta Pruning")
    print("Positions are numbered 0 to 8")

    while not game.game_over():

        game.print_board()

        user_move = int(input("Enter your move: "))

        if user_move not in game.available_moves():
            print("Invalid move")
            continue

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