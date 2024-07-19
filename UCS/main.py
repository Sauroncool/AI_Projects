from augment import graph
# from augment2 import graph
import heapq


def ucs(start, goal, forbidden_nodes=None):
    frontier = []  # Use a priority queue (min-heap)
    reached = set()
    parent = {}  # Store parents of each node
    cost = {}  # Store cost to reach each node

    heapq.heappush(frontier, (0, start))  # Push tuple (cost, node)
    reached.add(start)
    cost[start] = 0

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = [goal]
            current = goal

            while current != start:
                path.append(parent[current])
                current = parent[current]
            path.reverse()

            print("Path found: {}".format(path))
            return path

        for child in children(current_node):
            new_cost = current_cost + cost_to_reach(current_node, child)  # Replace with your cost function

            if (child not in reached or new_cost < cost[child]) and (forbidden_nodes is None or child not in forbidden_nodes):
                reached.add(child)
                cost[child] = new_cost
                parent[child] = current_node
                heapq.heappush(frontier, (new_cost, child))


# Define a function to return children of current node
def children(v):
    if v in graph.Graph:
        children = [name for name, distance in graph.Graph[v]]
        return children
    else:
        return None

def cost_to_reach(from_node, to_node):
    for neighbor, cost in graph.Graph.get(from_node, []):
         if neighbor == to_node:
            return cost
    return float('inf')  # Return infinity if no direct connection found


start = 'H1'
goal = 'H7'
ucs(start, goal, graph.forbidden_nodes)

# start = 'Arad'
# goal = 'Bucharest'
# ucs(start, goal)
