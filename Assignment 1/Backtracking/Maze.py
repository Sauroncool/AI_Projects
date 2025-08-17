# Solve a 2D maze by backtracking.
# By Ambuj
# Print statements can be uncommented in recursive_backtracking.py to see the whole process, i.e. how the program moved
# forward and backtracked.

from recursive_backtracking import *
import time

class MazeProblem:
    def __init__(self, maze):
        self.maze = maze
        # self.start = (0, 0)
        # self.end = (len(maze) - 1, len(maze[0]) - 1)
        self.start = (0, 10)    # Start Node
        self.end = (len(maze) - 1, 10)  # End Node
        self.visited = set()    # Create a visited list

    def is_complete(self, assignment):
        return self.end in assignment.values()  # If the assignment has end node

    def select_unassigned_variable(self, assignment):
        if not assignment:
            return self.start   # If assignment is empty return Start Node

        last_var = list(assignment.keys())[-1]  # Last Node
        neighbors = get_neighbors(last_var, self.maze)

        for neighbor in neighbors:
            if neighbor not in assignment and neighbor not in self.visited:
                self.visited.add(neighbor)  # Adding it to visited list.
                return neighbor

        return None

    def order_domain_values(self, var, assignment):
        return get_neighbors(var, self.maze)

    def is_consistent(self, var, value, assignment):
        return value not in assignment  # Checks whether value is already in assignment.


def solve_maze(maze):
    problem = MazeProblem(maze)
    assignment = backtracking(problem)
    if assignment is not None:
        return list(assignment.keys()) + [problem.end]
        # Returning Start, Path and End together.
    else:
        return "No solution found"


def get_neighbors(current, maze):
    if current is None:
        return []
    neighbors = []
    row, col = current
    if row > 0 and maze[row - 1][col] == 0:
        neighbors.append((row - 1, col))  # UP
    if col > 0 and maze[row][col - 1] == 0:
        neighbors.append((row, col - 1))  # LEFT
    if row < len(maze) - 1 and maze[row + 1][col] == 0:
        neighbors.append((row + 1, col))  # DOWN
    if col < len(maze[0]) - 1 and maze[row][col + 1] == 0:
        neighbors.append((row, col + 1))  # RIGHT
    return neighbors


# maze = [[0, 1, 1, 1, 1, 1],
#         [0, 1, 0, 1, 0, 1],
#         [0, 0, 0, 0, 0, 1],
#         [1, 0, 1, 1, 0, 1],
#         [0, 0, 0, 1, 0, 1],
#         [1, 1, 0, 0, 0, 0]]
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]

start_time=time.time()
answer = solve_maze(maze)
print(f'Time Taken = {time.time()-start_time} s')
print('Printing Maze')
for i in range(len(maze)):
    for j in range(len(maze[i])):
        print(str(maze[i][j]) + " ", end="")
    print("")

print(f'\nPath is {answer}')
print(f"Length of Path = {len(answer)}")

print('\nPath will look like this')
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if (i, j) in answer:
            print('*' + " ", end="")
        else:
            print('|' + " ", end="")
    print("")
