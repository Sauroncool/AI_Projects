# Problem
# In a city you can travel using either 3 options. Option 1 : Walk, will take 1 minute to walk 1 block
# Option 2 : Scooty, will take 2 minutes to travel 3 blocks (Only available in blocks divisible by 3, scooty won't work
# for 10% of the time, when it won't work you will lose time)
# Option 3 : Tram, will take 2 minutes to travel 5 blocks (Only available in blocks divisible by 5, Trams won't work for
# 30% of the time, when it won't work you will lose time)

import os
import sys

sys.setrecursionlimit(10000)


class TransportationMDP(object):
    def __init__(self, N):
        # N = Number of Blocks
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def actions(self, state):
        # Return a list of valid actions
        result = []
        if state + 1 <= self.N:
            result.append('walk')
        if (state + 3 <= self.N) & (state % 3 == 0):
            result.append('scooty')
        if (state + 5 <= self.N) & (state % 5 == 0):
            result.append('tram')
        return result

    def succProbReward(self, state, action):
        # return list of (newstate,prob,reward) triples
        # state = s, action = a, newState = s'
        # prob = T(s,a,s'), reward = Reward(s, a, s')
        result = []
        if action == 'walk':
            result.append((state + 1, 1, -1))
        elif action == 'scooty':
            result.append((state + 3, 0.9, -2))
            result.append((state, 0.1, -2))
        elif action == 'tram':
            result.append((state + 5, 0.7, -2))
            result.append((state, 0.3, -2))
        return result

    def discount(self):
        return 1

    def states(self):
        return range(1, self.N + 1)


# Inference (Algorithms)

def valueItereation(mdp):
    # Initialize
    V = {}  # state -> Vopt[state]
    for state in mdp.states():
        V[state] = 0

    def Q(state, action):
        return sum(prob * (reward + mdp.discount() * V[newState]) \
                   for newState, prob, reward in mdp.succProbReward(state, action))

    while True:
        # compute the new values (newV) given the old values (V)
        newV = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                newV[state] = 0
            else:
                newV[state] = max(Q(state, action) for action in mdp.actions(state))
        # check for convergence
        if max(abs(V[state] - newV[state]) for state in mdp.states()) < 1e-3:
            break
        V = newV

        # read out policy
        pi = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                pi[state] = 'none'
            else:
                pi[state] = max((Q(state, action), action) for action in mdp.actions(state))[1]

        # print stuff out
        os.system('cls')
        print('{:30} {:30} {:30}'.format('s', 'V(s)', 'pi(s)'))
        for state in mdp.states():
            print('{:30} {:30} {:30}'.format(state, V[state], pi[state]))
        #input()


mdp = TransportationMDP(N=30)
valueItereation(mdp)
