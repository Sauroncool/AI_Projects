# Solving N-Queen Problem by backtracking
# By Ambuj
# Print statements can be uncommented in recursive_backtracking.py to see the whole process, i.e. how the program moved
# forward and backtracked.

from recursive_backtracking import *
import time


class NQueensProblem:
    def __init__(self, n, initial_state):
        self.n = n
        if initial_state is None:
            self.initial_state = {}
        else:
            self.initial_state = initial_state
            self.assignment = initial_state.copy()

    def is_complete(self, assignment):
        return len(assignment) == self.n  # Returns whether number of queens is equal to length of assignment.

    def select_unassigned_variable(self, assignment):
        for i in range(self.n):
            if i not in assignment:
                return i

    def is_consistent(self, var, value, assignment):
        for other_var, other_value in assignment.items():
            if value == other_value and var != other_var:  # Check Column
                return False
            if abs(var - other_var) == abs(value - other_value) and var != other_var:  # Check diagonal
                return False
        return True

    def order_domain_values(self, var, assignment):
        initial_state = self.initial_state
        values = []
        if len(initial_state) != 0:
            values.extend([initial_state[var]])  # Taking the user input into account
        values.extend(list(range(self.n)))
        for value in assignment.values():
            if value in values:
                values.remove(value)    # If that column conflicts with other queens remove it.
        return values


def solve_n_queens(n, initial_state=None):
    problem = NQueensProblem(n, initial_state)
    return backtracking(problem)


# Input
n = 8

col_indices = []
row_indices = []
for i in range(0, n):
    col_indices.append(5)
    row_indices.append(i)

# col_indices = [3, 1, 6, 2, 5, 7, 0, 4]
# row_indices = [0, 1, 2, 3, 4, 5, 6, 7]

initial_state = {row: col for row, col in zip(row_indices, col_indices)}
# initial_state = {}
print(f'Initial State = {initial_state}')

start_time = time.time()
solution = solve_n_queens(n, initial_state)
print(f'Time={time.time() - start_time} s')
print(f'Solution = {solution}')
# Printing in the format of row and column
