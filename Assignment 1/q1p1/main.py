from augment import graph
import time

graph.generate() #Generate the problem as tree and store it in {Graph}

start_time = time.time()

def aStar(start, goal):
    frontier = set()
    reached = set()
    g = {} #Store distance from start
    cameFrom = {} #Store the optimal parents of each relevant node

    g[start] = 0
    #Since start is the root node, its parent is set to itself
    cameFrom[start] = start
    frontier.add(start)
    while len(frontier) > 0:
        n = None

        #Search for the node to expand with the lowest f function
        for v in frontier:
            if n==None or g[v] + graph.heur(v) < g[n] + graph.heur(n): #heur is the user-defined heuristic function
                n = v

        if n == goal or graph.Graph[n] == None:
            pass
        else:
            for (m, sep) in children(n): #sep is the separation between node n and its child m
                #nodes not in frontier and reached are added to frontier & n is set its parent
                if m not in frontier and m not in reached:
                    frontier.add(m)
                    cameFrom[m] = n
                    g[m] = g[n] + sep

                else:
                    if g[m] > g[n] + sep:
                        g[m] = g[n] + sep #update g[m]
                        cameFrom[m] = n #update optimal parent of m

                        #if m is in reached, remove and add it to frontier to expand through the new path
                        if m in reached:
                            reached.remove(m)
                            frontier.add(m)

        if n == None:
            print("Path does not exist")
            return None

        #If the current node is the goal, then we begin reconstructing the path
        #from it to the start node using the cameFrom dictionary
        if n == goal:
            path = []

            while cameFrom[n] != n:
                path.append(n)
                n = cameFrom[n]
            path.append(start)
            path.reverse()

            print("Path found: {}".format(path))
            graph.output(path)
            return

        #Remove n from frontier and put it into reached
        #because all its children were inspected
        frontier.remove(n)
        reached.add(n)

    print("Path does not exist")
    return None

print(time.time()-start_time) #Time taken for the processor to obtain the path from goal from the start in seconds

#Define a funcction to return children of current node and their distance to the current node
def children(v):
    if v in graph.Graph:
        return graph.Graph[v]
    else:
        return None

aStar(graph.start,graph.goal)
