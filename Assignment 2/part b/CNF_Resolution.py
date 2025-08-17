def PL_Resolution(clauses):
    # KB is a sentence in propositional logic
    # query is the propositional logic sentence to check for contradiction with the KB
    # A list containing clauses which are separated by and in CNF
    new = []
    while (True):
        # print(clauses)
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = Resolve(clauses[i], clauses[j])
                if resolvents is not None:  # Ensuring that resolvents has some output
                    if not resolvents:  # Checking whether resolvents is an Empty List
                        # Note- (if not resolvents) is true for both empty list and None output.
                        # print(clauses[i])
                        # print(clauses[j])
                        return True
                    if resolvents not in new:
                        new.append(resolvents)  # Adding resolvents into list named new.
        if all(item in clauses for item in new):  # If 'new' is a subset of 'clauses'
            return False
        clauses.extend(new)


def Resolve(Ci, Cj):
    # Find the complementary literals in the two clauses
    for literal in Ci:
        if literal[0] == '~':
            if literal[1:] in Cj:  # Checking if 'literal' is present in Cj for '~literal' in Ci
                # Combine the two clauses
                resolved_clause = set(Ci) | set(Cj)
                # Remove complementary literals
                resolved_clause.remove(literal)
                resolved_clause.remove(literal[1:])
                # Return the resolved clause
                for literal in list(resolved_clause):
                    if ('~' + literal) in list(resolved_clause):  # Check if the resolved clause contains
                        # complementary literals, because that will always be true.
                        return None
                return list(resolved_clause)

        if ('~' + literal) in Cj:  # Checking if '~literal' is present in Cj for 'literal' in Ci
            # Combine the two clauses
            resolved_clause = set(Ci) | set(Cj)
            # Remove complementary literals
            resolved_clause.remove(literal)
            resolved_clause.remove('~' + literal)
            # Return the resolved clause
            for literal in list(resolved_clause):
                if ('~' + literal) in list(resolved_clause):  # Check if the resolved clause contains complementary
                    # literals, because that will always be true.
                    return None
            return list(resolved_clause)
    # If no complementary literals were found, return None
    return None


statement1 = [['~p21', 'b11'], ['~b11', 'p12', 'p21'], ['~p12', 'b11'], ['~b11'], ['p12']]
statement2 = [['p1', 'p2'], ['~p1', 'p3'], ['~p2', 'p3'], ['~p3', 'p4'], ['~p4', 'p5'], ['~p5']]

print(f'Knowledge Base = {statement1[:-1]}')
print(f'Negation of Query={statement1[-1]}')
print(PL_Resolution(statement1))
print(f'Knowledge Base = {statement2[:-1]}')
print(f'Negation of Query={statement2[-1]}')
print(PL_Resolution(statement2))
