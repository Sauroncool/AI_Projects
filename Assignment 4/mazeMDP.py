import sys
import os

sys.setrecursionlimit(10000)


class MazeMDP(object):
    def __init__(self, maze):
        # N = Number of Blocks
        self.maze = maze
        self.start = (0, 10)  # Start Node
        self.end = (len(maze) - 1, 10)  # End Node

    def startState(self):
        return self.start

    def isEnd(self, state):
        return state == self.end

    def actions(self, state):
        # Return a list of valid actions
        result = []
        row, col = state
        if row > 0 and self.maze[row - 1][col] == 'O':
            result.append('UP')  # UP
        if col > 0 and self.maze[row][col - 1] == 'O':
            result.append('LEFT')  # LEFT
        if row < len(self.maze) - 1 and self.maze[row + 1][col] == 'O':
            result.append('DOWN')  # DOWN
        if col < len(self.maze[0]) - 1 and self.maze[row][col + 1] == 'O':
            result.append('RIGHT')  # RIGHT
        return result

    def succProbReward(self, state, action):
        # return list of (newstate,prob,reward) triples
        # state = s, action = a, newState = s'
        # prob = T(s,a,s'), reward = Reward(s, a, s')
        result = []
        row, col = state
        if action == 'UP':
            newState = (row - 1, col)
        elif action == 'LEFT':
            newState = (row, col - 1)
        elif action == 'DOWN':
            newState = (row + 1, col)
        elif action == 'RIGHT':
            newState = (row, col + 1)

        if newState == self.end:
            reward = 50
        elif newState == self.start:
            reward = 0
        else:
            reward = -1

        return [(newState, 1, reward)]

    def discount(self):
        return 1

    def states(self):
        return [(i, j) for i in range(len(self.maze)) for j in range(len(self.maze[0])) if self.maze[i][j] == 'O']


def valueIteration(mdp):
    # Initialize
    V = {}  # state -> Vopt[state]
    for state in mdp.states():
        V[state] = 0

    def Q(state, action):
        return sum(prob * (reward + mdp.discount() * V[newState]) for newState, prob, reward in
                   mdp.succProbReward(state, action))

    for num in range(800):
        # compute the new values (newV) given the old values (V)
        newV = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                newV[state] = 0
            else:
                newV[state] = max(Q(state, action) for action in mdp.actions(state))

        V = newV
        # print(V)
        # read out policy
        pi = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                pi[state] = 'none'
            else:
                pi[state] = max((Q(state, action), action) for action in mdp.actions(state))[1]
    print(V)
    key = mdp.start
    path = [mdp.start]
    while not V[key] == max(V[k] for k in V):
        for key1 in V:
            if V[key1] == V[key] + 1 and (abs(key[0] - key1[0]) + abs(key[1] - key1[1]) == 1):
                path.append(key1)
                key = key1
                break

    path.append(mdp.end)
    print(path)

    print([pi[key] for key in path])

    print('\nPath will look like this')
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) in path:
                print('*' + " ", end="")
            else:
                print('|' + " ", end="")
        print("")


maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
        ['X', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X'],
        ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X']]

print('Printing Maze')
for i in range(len(maze)):
    for j in range(len(maze[i])):
        print(str(maze[i][j]) + " ", end="")
    print("")

mdp = MazeMDP(maze)
valueIteration(mdp)
