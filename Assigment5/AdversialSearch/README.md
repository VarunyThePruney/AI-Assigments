# Adversarial Search Algorithms in Python

## Overview

This project implements four important adversarial search algorithms used in Artificial Intelligence:

1. Minimax Search
2. Alpha-Beta Pruning
3. Heuristic Alpha-Beta Search
4. Monte Carlo Tree Search (MCTS)

All algorithms are implemented using the Tic-Tac-Toe game environment in Python.

---

# Folder Structure

```text
Assigment5/
│
├── AdversialSearch/
│   │
│   ├── minimax.py
│   ├── alpha_beta.py
│   ├── heuristic_alpha_beta.py
│   ├── monte_carlo_tree_search.py
│   │
│   └── games/
│       ├── __init__.py
│       └── tic_tac_toe.py
```

---

# Requirements

* Python 3.x

No external libraries are required.

---

# How to Run

Run the scripts from the project root directory.

## Minimax

```bash
python3 -m Assigment5.AdversialSearch.minimax
```

---

## Alpha-Beta Pruning

```bash
python3 -m Assigment5.AdversialSearch.alpha_beta
```

---

## Heuristic Alpha-Beta Search

```bash
python3 -m Assigment5.AdversialSearch.heuristic_alpha_beta
```

---

## Monte Carlo Tree Search

```bash
python3 -m Assigment5.AdversialSearch.monte_carlo_tree_search
```

---

# Game Rules

The game uses Tic-Tac-Toe with board positions numbered from 0 to 8.

```text
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

Player:

* O

AI:

* X

---

# Algorithms

## 1. Minimax Search

Minimax is a complete adversarial search algorithm.

The algorithm:

* explores all possible future moves
* assumes both players play optimally
* chooses the move with the best guaranteed outcome

### Advantages

* Always optimal
* Simple to understand

### Disadvantages

* Slow for large search spaces
* Explores many unnecessary branches

---

## 2. Alpha-Beta Pruning

Alpha-Beta pruning improves Minimax performance by eliminating branches that cannot affect the final decision.

### Key Concepts

* Alpha:
  Best score achievable by the maximizing player.

* Beta:
  Best score achievable by the minimizing player.

### Advantages

* Faster than Minimax
* Produces the same optimal result

### Disadvantages

* Still expensive for very large games

---

## 3. Heuristic Alpha-Beta Search

This version introduces:

* depth-limited search
* heuristic board evaluation

Instead of exploring the full game tree, the search stops at a fixed depth and estimates board quality using heuristics.

### Heuristic Evaluation

The evaluation function:

* rewards positions favorable to AI
* penalizes positions favorable to the opponent

### Advantages

* Faster than complete search
* Scales better to larger games

### Disadvantages

* May not always produce optimal moves
* Depends on heuristic quality

---

## 4. Monte Carlo Tree Search (MCTS)

Monte Carlo Tree Search uses random simulations to estimate the best move.

The algorithm has four stages:

1. Selection
2. Expansion
3. Simulation
4. Backpropagation

### Advantages

* Works well for very large search spaces
* Does not require complete tree exploration

### Disadvantages

* Results depend on number of simulations
* Randomness can affect move quality

---
# Test Cases

## Test Case 1 — Minimax Winning Move

### Input Board

```text
X | X |  
---------
O | O |  
---------
  |   |  
```

### Expected Result

AI selects position 2 and wins the game.

### Output

```text
AI chose position 2
AI wins!
```

---

# Test Case 2 — Alpha-Beta Blocking Move

### Input Board

```text
O | O |  
---------
X |   |  
---------
  | X |  
```

### Expected Result

AI blocks opponent at position 2.

### Output

```text
AI chose position 2
```

---

# Test Case 3 — Heuristic Alpha-Beta Evaluation

### Input Board

```text
X |   |  
---------
  | O |  
---------
  |   | X
```

### Expected Result

AI chooses a strategically strong position using heuristic evaluation.

### Output

```text
AI chose optimal heuristic move
```

---

# Test Case 4 — Monte Carlo Tree Search

### Input Board

```text
X | O | X
---------
O | X |  
---------
  |   | O
```

### Expected Result

MCTS selects one of the statistically strongest moves after simulations.

### Output

```text
AI chose position 6
```

---

# Test Case 5 — Draw Detection

### Input Board

```text
X | O | X
---------
X | O | O
---------
O | X | X
```

### Expected Result

Game ends in draw.

### Output

```text
Draw!
```

---

# Test Case 6 — Invalid Move Handling

### Input

Player enters an already occupied position.

### Expected Result

Program rejects the move.

### Output

```text
Invalid move
```

---

# Conclusion

This project demonstrates different adversarial search strategies used in Artificial Intelligence.

The implementations show:

* complete search methods
* pruning optimization
* heuristic evaluation
* probabilistic simulation-based search

These algorithms are foundational techniques used in game AI and decision-making systems.
