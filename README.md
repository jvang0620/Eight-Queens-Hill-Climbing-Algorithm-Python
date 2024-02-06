# Eight-Queens Problem Solver

### Overview:

This program implements a solution to the classic N-Queens problem using a hill climbing algorithm. The Eight-Queens problem involves placing 8 chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.

This program was created from the ground up, drawing inspiration from various sources.

### Example of Program Output Screenshots

![Examples Of Program](/imgs/img_1a.PNG)
![Examples Of Program](/imgs/img_1b.PNG)

##### 'Current h' Meaning:

- `"Current h"` stands for "Current heuristic value." The heuristic value represents an estimation of how close a given state is to the goal state in the N-Queens problem. It's a measure of how many conflicts (queens attacking each other) exist in the current state

##### 'Neighbors found with lower h' Meaning:

- `"Neighbors found with lower h"` refers to the number of neighboring states (or configurations of the N-Queens board) where the heuristic value is lower than the heuristic value of the current state. In the context of the N-Queens problem solved by a hill climbing algorithm, "lower h" indicates states that are closer to the goal state, as they have fewer conflicts among the queens.

- When the program prints `"Neighbors found with lower h,"` it's indicating how many neighboring states have been found where the heuristic value (h) is lower, suggesting potential moves that might lead to an improvement in the current state. This information helps in deciding whether to make a move to a neighbor or perform a random restart if no better neighbors are found.

##### 'State changes' and 'Restart' Meaning:

- When the solution is found in the context of the N-Queens problem solved by a hill climbing algorithm, `"state changes"` refers to the number of times the algorithm transitioned from one state to another during its search process. Each state change represents a move made by the algorithm, either to a neighboring state with a lower heuristic value or as a result of a random restart.

- `"Restarts"` indicates the number of times the algorithm performed a random restart. A random restart occurs when the algorithm gets stuck in a local minimum, meaning it cannot find any neighboring states with lower heuristic values. In such cases, the algorithm resets to a new random initial state and continues its search for a solution from there.

### Features:

- **Hill Climbing Algorithm**: The program employs a hill climbing algorithm to iteratively improve the placement of queens on the board until a solution is found.

- **Random Restart**: If the algorithm reaches a local maximum where no better moves are possible, it performs a random restart to escape from local optima.

- **Heuristic Evaluation**: The heuristic function evaluates the quality of a state based on the number of conflicts between queens, aiding in the decision-making process to select the best neighbor state.

### Components:

- **Main Class**: The entry point of the program. It orchestrates the solving process and prints the final solution.

- **State Generation**: The generateRandomState() method initializes a random state representing the initial placement of queens on the board.

- **Goal State Check**: The isGoalState() method determines whether a given state satisfies the conditions of a solution.

- **Neighbor Selection**: The getBestNeighbor() method identifies the best neighbor state with the lowest heuristic value.

- **Heuristic Calculation**: The calculateHeuristic() method computes the heuristic value for a given state based on the number of conflicts.

- **Board Visualization**: The printBoard() method displays the current state of the board, facilitating visualization of queen placements.

### Getting Started:

1. Clone the repository to your local machine with one of the follow:

   HTTPS: <pre><code>git clone https://github.com/jvang0620/Eight-Queens-Hill-Climbing-Algorithm-Python</code></pre>
   SSH: <pre><code>git clone https://github.com/jvang0620/Eight-Queens-Hill-Climbing-Algorithm-Python</code></pre>

2. **Compile/Run**: Compile the Python source code and run the applicaiton using `python main.py`.
3. **Output**: The program will display the progress of the solution process, including the current state, heuristic values, and solution details.

### Developed Using:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Source:

[N-Queens Problem](https://rosettacode.org/wiki/N-queens_problem#Java)
[N-Queen Problem | Local Search using Hill climbing with random neighbour](https://www.geeksforgeeks.org/n-queen-problem-local-search-using-hill-climbing-with-random-neighbour/#)
