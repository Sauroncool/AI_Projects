def PL_Resolution(KB, query):
    #KB is a sentence in propositional logic
    #query is the propositional logic sentence to check for contrdiction with the KB
    if query[0] == '~':
        clauses = toCNF('(' + KB + ')' + ' and ' + query[1:]) #A list containing clauses which are separated by 'and' in CNF
    clauses = toCNF('(' + KB + ')' + ' and ' + '~' + query)
    new = [] #Stores the updated set of clauses after processing
    while True:
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                resolvents = Resolve(clauses[i],clauses[j]) #Resolve each pair of clauses
                if resolvents is not None:
                    if not resolvents: #Checking if we have arrived at an empty clause
                        return True #Return that we have arrived at a contradiction and the query can be added to KB
                    new.append(resolvents)
        if all(x in new for x in clauses): #Checking if the new set of clauses is a subset of clauses
            return False
        clauses.extend(new) #Update the set of clauses with the new set

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

print(PL_Resolution(KB1,q1)) #Example 1
KB1 = (B11 <=> (P12 or P21)) and ~B11
q1 = ~P12

# print(PL_Resolution(KB2,q2)) #Example 2
# KB2 =
# q2 =
