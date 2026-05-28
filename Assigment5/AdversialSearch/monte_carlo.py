# monte_carlo_tree_search.py

import random
import math
from copy import deepcopy

from .games.tic_tac_toe import TicTacToe


SIMULATIONS = 1000


class Node:

    def __init__(self, game, parent=None, move=None):

        self.game = game
        self.parent = parent
        self.move = move

        self.children = []

        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self):

        return len(self.children) == len(self.game.available_moves())

    def best_child(self, exploration_weight=1.41):

        best_score = -float("inf")
        best_node = None

        for child in self.children:

            if child.visits == 0:
                score = float("inf")

            else:
                exploitation = child.wins / child.visits

                exploration = exploration_weight * math.sqrt(
                    math.log(self.visits) / child.visits
                )

                score = exploitation + exploration

            if score > best_score:
                best_score = score
                best_node = child

        return best_node


def random_playout(game, current_player):

    while not game.game_over():

        move = random.choice(game.available_moves())

        game.make_move(move, current_player)

        current_player = "O" if current_player == "X" else "X"

    if game.winner("X"):
        return 1

    elif game.winner("O"):
        return -1

    return 0


def expand(node, player):

    tried_moves = [child.move for child in node.children]

    possible_moves = game_moves = node.game.available_moves()

    untried_moves = [
        move for move in possible_moves
        if move not in tried_moves
    ]

    move = random.choice(untried_moves)

    new_game = deepcopy(node.game)

    new_game.make_move(move, player)

    child_node = Node(
        new_game,
        parent=node,
        move=move
    )

    node.children.append(child_node)

    return child_node


def backpropagate(node, result):

    while node is not None:

        node.visits += 1

        if result == 1:
            node.wins += 1

        node = node.parent


def mcts(root_game):

    root = Node(deepcopy(root_game))

    for _ in range(SIMULATIONS):

        node = root

        game_copy = deepcopy(root_game)

        current_player = "X"

        # Selection
        while node.children and node.is_fully_expanded():

            node = node.best_child()

            game_copy.make_move(node.move, current_player)

            current_player = "O" if current_player == "X" else "X"

        # Expansion
        if not game_copy.game_over():

            node = expand(node, current_player)

            game_copy = deepcopy(node.game)

            current_player = "O" if current_player == "X" else "X"

        # Simulation
        result = random_playout(game_copy, current_player)

        # Backpropagation
        backpropagate(node, result)

    # Choose best move
    best_child = max(
        root.children,
        key=lambda child: child.visits
    )

    return best_child.move


if __name__ == "__main__":

    game = TicTacToe()

    print("Monte Carlo Tree Search")
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

        ai_move = mcts(game)

        game.make_move(ai_move, "X")

        print(f"AI chose position {ai_move}")

    game.print_board()

    if game.winner("X"):
        print("AI wins!")

    elif game.winner("O"):
        print("You win!")

    else:
        print("Draw!")