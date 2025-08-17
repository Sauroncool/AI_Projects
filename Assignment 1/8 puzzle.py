from collections import deque


# Check if a puzzle state is solvable or not
def is_solvable(puzzle):
    inversion = 0
    for i in range(8):
        for j in range(i + 1, 9):
            # Count number of inversions
            if puzzle[i] and puzzle[j] and puzzle[i] > puzzle[j]:
                inversion += 1
    # Return True if number of inversions is even, else False
    return inversion % 2 == 0


# Breadth-first search function to find the solution
def bfs(start, end):
    # Initialize queue with start node
    q = deque([start])
    # Add start node to visited set
    visited = set([start])
    # Initialize dictionary to store parent of each node
    parent = {}
    # Loop until queue is empty
    while q:
        # Dequeue a node from the queue
        node = q.popleft()
        # Check if the node is the goal state
        if node == end:
            return parent, node
        # Get all neighbors of the node
        for nei in get_neighbors(node):
            # Add unvisited neighbors to the queue and visited set
            if nei not in visited:
                q.append(nei)
                visited.add(nei)
                parent[nei] = node
    # Return None if no solution is found
    return None, None


# Function to get all neighbors of a puzzle state
def get_neighbors(puzzle):
    # Get index of blank tile (0)
    index = puzzle.index(0)
    row, col = index // 3, index % 3
    neighbors = []
    # Move blank tile up if possible
    if row > 0:
        copy = list(puzzle)
        copy[index], copy[index - 3] = copy[index - 3], copy[index]
        neighbors.append(tuple(copy))
    # Move blank tile down if possible
    if row < 2:
        copy = list(puzzle)
        copy[index], copy[index + 3] = copy[index + 3], copy[index]
        neighbors.append(tuple(copy))
    # Move blank tile left if possible
    if col > 0:
        copy = list(puzzle)
        copy[index], copy[index - 1] = copy[index - 1], copy[index]
        neighbors.append(tuple(copy))
    # Move blank tile right if possible
    if col < 2:
        copy = list(puzzle)
        copy[index], copy[index + 1] = copy[index + 1], copy[index]
        neighbors.append(tuple(copy))
    # Return list of all neighbors
    return neighbors


# Function to print a puzzle state
def print_puzzle(puzzle):
    for i in range(9):
        # Add newline after every 3 elements
        if i % 3 == 0:
            print()
        print(puzzle[i], end=" ")
    # Add newline after last element
    print("\n")


# Function to solve the 8-puzzle problem
def solve(start, end):
    # Check if start puzzle state is solvable or not
    if not is_solvable(start) or not is_solvable(end):
        print("The puzzle is unsolvable.")
        return

    # Call BFS function to find the solution
    parent, node = bfs(start, end)

    # If solution is not found, return
    if not node:
        print("No solution found.")
        return
    
    while node:
        print_puzzle(node)
        node = parent.get(node, None)


# Initialize start and end puzzle states
start = (1, 2, 3, 4, 5, 6, 0, 7, 8)
end = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# Call the solve function to solve the puzzle
solve(end, start)
