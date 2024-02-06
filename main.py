import random

def main():
    solution = solve_queens_problem()
    print_board(solution)

def solve_queens_problem():
    current_state = generate_random_state()

    solution = current_state
    state_changes = 0
    restarts = 0

    while not is_goal_state(current_state):
        neighbor = get_best_neighbor(current_state)
        current_heuristic = calculate_heuristic(current_state)

        print()
        print("Current h:", current_heuristic)
        print_board(current_state)

        lower_heuristic = current_heuristic - calculate_heuristic(neighbor)
        print("Neighbors found with lower h:", lower_heuristic)

        if lower_heuristic == 0:
            print("RESTART")
            current_state = generate_random_state()
            restarts += 1
        else:
            print("Setting new current state")
            current_state = neighbor
            state_changes += 1

        if calculate_heuristic(current_state) < calculate_heuristic(solution):
            solution = current_state

    print()
    print("***Solution Found!***")
    print("Current State")
    print("State changes:", state_changes)
    print("Restarts:", restarts)

    return solution

def generate_random_state():
    state = [random.randint(0, 7) for _ in range(8)]
    return state

def is_goal_state(state):
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                return False
    return True

def get_best_neighbor(state):
    best_neighbor = state[:]
    current_heuristic = calculate_heuristic(state)

    for i in range(len(state)):
        for j in range(len(state)):
            neighbor = state[:]
            neighbor[i] = j
            neighbor_heuristic = calculate_heuristic(neighbor)

            if neighbor_heuristic < current_heuristic:
                best_neighbor = neighbor
                current_heuristic = neighbor_heuristic

    return best_neighbor

def calculate_heuristic(state):
    heuristic = 0

    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                heuristic += 1

    return heuristic

def print_board(state):
    board = [[0] * 8 for _ in range(8)]

    for i in range(len(state)):
        board[state[i]][i] = 1

    print("Current State")
    for row in board:
        print(','.join(map(str, row)))

if __name__ == "__main__":
    main()
