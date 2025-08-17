from graph2 import mape
from heurAIR import H
from travel_speed import *


class find:
    Graph = {}

    def aStar(start, goal):
        find.Graph = mape.draw(start, goal)
        frontier = set()
        frontier.add(start)
        reached = set()
        g = {}  # store distance from start
        cameFrom = {}  # store the optimal parents of each relevant node
        elat = H.numbify(goal)[0]
        elon = H.numbify(goal)[1]

        g[start] = 0
        speed = travel_speed(H.numbify(start)[0], H.numbify(start)[1], elat, elon)
        # Since start is the root node, its parent is set to itself
        cameFrom[start] = start

        while len(frontier) > 0:
            n = None

            # Search for the node to expand with the lowest f function
            for v in frontier:
                #print(v,n)

                if n == None or g[v] + H.heuristic(H.numbify(v), H.numbify(goal), H.numbify(v), H.numbify(goal),
                                                   speed) < g[
                    n] + H.heuristic(H.numbify(n), H.numbify(goal), H.numbify(n), H.numbify(goal),
                                     speed):  # heur is the user-defined heuristic function
                    n = v
            #print(n)
            if n == goal or find.Graph[n] == None:
                pass
            else:
                for (m, sep) in find.children(n):  # sep is the separation between node n and its child m
                    # nodes not in frontier and reached are added to frontier & n is set its parent
                    print(m,sep)
                    if m not in frontier and m not in reached:
                        frontier.add(m)
                        cameFrom[m] = n
                        g[m] = g[n] + sep

                    else:
                        if g[m] > g[n] + sep:
                            g[m] = g[n] + sep  # update g[m]
                            cameFrom[m] = n  # update optimal parent of m

                            # if m is in reached, remove and add it to frontier
                            if m in reached:
                                reached.remove(m)
                                frontier.add(m)

            if n == None:
                print("Path does not exist")
                return None

            # If the current node is the goal, then we begin reconstructing the path
            # from it to the start node using the cameFrom dictionary
            if n == goal:
                path = []

                while cameFrom[n] != n:
                    path.append(n)
                    n = cameFrom[n]
                path.append(start)
                path.reverse()

                print("Path found: {}".format(path))
                return path

            # Remove n from frontier and put it into reached
            # because all its children were inspected
            frontier.remove(n)
            reached.add(n)

        print("Path does not exist")
        return None

    def children(v):
        if v in find.Graph:
            #print('idr dekho',find.Graph[v])
            return find.Graph[v]
        else:
            return None
