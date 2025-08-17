def backtracking(problem):
    return recursive_backtracking({}, problem)


def recursive_backtracking(assignment, problem):
    if problem.is_complete(assignment):
        # returns True if assignment is complete (Depends on function),False otherwise.
        return assignment

    var = problem.select_unassigned_variable(assignment)
    # returns an unassigned variable that should be assigned next. This is the problem-specific heuristic.
    for value in problem.order_domain_values(var, assignment):
        # returns a list of values in the domain of variable var in a specific order. This is the problem-specific
        # heuristic.
        if problem.is_consistent(var, value, assignment):
            # returns True if assigning value to var in assignment is consistent with the problem's constraints,
            # False otherwise. If not, it selects an unassigned variable and tries all values in its domain in a
            # specific order, checking if each value is consistent with the problem's constraints.
            assignment[var] = value
            result = recursive_backtracking(assignment, problem)
            # If it finds a consistent value, it assigns it to the variable and recursively calls itself.
            if result is not None:
                return result
            #  If the recursive call returns a non-None result, it means that a complete and consistent assignment was
            # found, so it returns that result.
            del assignment[var]
            # If result is none, it backtracks by removing the variable assignment and trying the next value in its
            # domain.
    return None
