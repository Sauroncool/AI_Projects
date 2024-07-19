from augment import graph
# from augment import graph

def dfs(start, goal, forbidden_nodes=None):
    frontier = list()
    reached = list()
    parent = {}  # Store the  parents of each node

    frontier.append(start)
    reached.append(start)

    while frontier:
        # print(frontier)
        current_node = frontier.pop()
        # print(current_node)
        # print(children(current_node))

        for child in children(current_node):

            #nodes not in  reached are added to frontier
            if child not in reached and (forbidden_nodes is None or child not in forbidden_nodes):
                frontier.append(child)
                reached.append(child)
                parent[child] = current_node

                if child == goal:
                    path = [goal]
                    current = goal

                    while current != start:
                        path.append(parent[current])
                        current = parent[current]
                    path.reverse()

                    print("Path found: {}".format(path))
                    return
        # print(frontier)

    print("Path does not exist")
    return None


# Define a function to return children of current node
def children(v):
    if v in graph.Graph:
        children = [name for name, distance in graph.Graph[v]]
        return children
    else:
        return None


start = 'H1'
goal = 'H7'
dfs(start, goal, graph.forbidden_nodes)

# start = 'Arad'
# goal = 'Bucharest'
# dfs(start, goal)
