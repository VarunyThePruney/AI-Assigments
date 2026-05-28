# heuristic_alpha_beta.py

from .games.tic_tac_toe import TicTacToe


MAX_DEPTH = 3


def evaluate_board(game):

    score = 0
    #small set of winning states to evaluate the board
    winning_lines = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for line in winning_lines:

        values = [game.board[i] for i in line]

        # AI advantage
        if values.count("X") == 2 and values.count(" ") == 1:
            score += 10

        elif values.count("X") == 1 and values.count(" ") == 2:
            score += 1

        # Opponent advantage
        if values.count("O") == 2 and values.count(" ") == 1:
            score -= 10

        elif values.count("O") == 1 and values.count(" ") == 2:
            score -= 1

    return score


def heuristic_alpha_beta(game, depth, alpha, beta, maximizing):

    # Terminal states
    if game.winner("X"):
        return 100

    if game.winner("O"):
        return -100

    if game.is_draw():
        return 0

    # Depth limit reached
    if depth == MAX_DEPTH:
        return evaluate_board(game)

    # Maximizing player
    if maximizing:

        best_score = -float("inf")

        for move in game.available_moves():

            game.make_move(move, "X")

            score = heuristic_alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                False
            )

            game.undo_move(move)

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            if beta <= alpha:
                break

        return best_score

    # Minimizing player
    else:

        best_score = float("inf")

        for move in game.available_moves():

            game.make_move(move, "O")

            score = heuristic_alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                True
            )

            game.undo_move(move)

            best_score = min(best_score, score)

            beta = min(beta, best_score)

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

        score = heuristic_alpha_beta(
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

    print("Heuristic Alpha-Beta Search")
    print("Board positions: 0 to 8")

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