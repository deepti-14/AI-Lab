import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.depth + self.calculate_heuristic()

    def calculate_heuristic(self):
        # Number of misplaced tiles heuristic (h(n))
        goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]  # Final state
        misplaced = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != goal_state[i][j]:
                    misplaced += 1
        return misplaced

    def __lt__(self, other):
        return self.cost < other.cost

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def generate_moves(node):
    x, y = get_blank_position(node.state)
    possible_moves = []

    # Define possible moves: Up, Down, Left, Right
    moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    move_names = ['Up', 'Down', 'Left', 'Right']

    for (new_x, new_y), move_name in zip(moves, move_names):
        if is_valid_move(new_x, new_y):
            new_state = [row[:] for row in node.state]  # Create a copy of the current state
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            possible_moves.append((new_state, move_name))

    return possible_moves

def print_solution(node):
    path = []
    while node:
        if node.move is not None:
            path.append((node.move, node.state, node.cost - node.calculate_heuristic(), node.calculate_heuristic()))
        node = node.parent
    path.reverse()
    for move, state, f, h in path:
        print(f"Move: {move}")
        print('\n'.join([' '.join(map(str, row)) for row in state]))
        print(f"h(n) = {h}, f(n) = {f}")
        print()

def solve_puzzle(initial_state, goal_state):
    initial_node = PuzzleNode(initial_state)
    priority_queue = [initial_node]
    heapq.heapify(priority_queue)
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.state == goal_state:
            print("Solution Found!")
            print_solution(current_node)
            return

        visited.add(tuple(map(tuple, current_node.state)))

        for next_state, move in generate_moves(current_node):
            if tuple(map(tuple, next_state)) not in visited:
                next_node = PuzzleNode(next_state, current_node, move, current_node.depth + 1)
                heapq.heappush(priority_queue, next_node)

    print("No solution found.")
    # [2, 8, 3],
    # [1, 6, 4],
    # [7, 0, 5]


# Example usage:
initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]
 

goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

solve_puzzle(initial_state, goal_state)