from fringes import *
from problems import *
from math import sqrt

def manhattaDistance(Pos,Goal):
    minHeuristic = 999999
    for g in Goal:
        h = abs( Pos[0] - g[0]) + abs( Pos[1] - g[1])
        if h < minHeuristic:
            minHeuristic = h 
    return minHeuristic

def euclideanDistance(Pos,Goal):
    minHeuristic = 999999
    for g in Goal:
        h = sqrt((g[0] - Pos[0])**2 + abs(g[1] - Pos[1])**2)
        if h < minHeuristic:
            minHeuristic = h 
    return minHeuristic

def nullDistance(Pos,Goal):
    return 0

def ucs(problem):
    visited = []
    pqueue = Queue()
    pqueue.add(((problem.InitialState, []), 0))

    while not pqueue.isEmpty():

        (curPos, actions), cost = pqueue.remove()

        if curPos not in visited:
            visited.append(curPos)
            flag = problem.goalTest(curPos)
            if flag > 0:
                return actions + ['Stop']
            elif flag < 0:
                visited = []
                pqueue.clear()
                pqueue.add(((curPos, actions), 0))
            else:

                successors = problem.getSuccessors(curPos)

                for nPos, d in successors:
                    nActions = actions + [d]
                    ncost = cost + 1
                    pqueue.add(((nPos, nActions), ncost))
    return actions


def astar(problem, heuristic=nullDistance):
    pqueue = PriorityQueue()
    visited = []
    pqueue.add(0, problem.InitialState, [])
    while not pqueue.isEmpty():
        w , actions, curNode = pqueue.remove()
        visited.append((curNode.Pos, actions))
        flag = problem.goalTest(curNode)
        if flag > 0:
            return actions + ["Stop"]
        elif flag < 0:
            visited = []
            pqueue = PriorityQueue()
            pqueue.add(0,curNode,actions)
            
        else:
            successors = problem.getSuccessors(curNode)
            for nNode, d in successors:
                already_explored = False
                for v in visited:
                    vPos, vCost = v
                    if (vPos == nNode.Pos) and (len(actions) >= len(vCost)):
                        already_explored = True
                if not already_explored:
                    nActions = actions + [d]    
                    w = len(actions)+heuristic(nNode.Pos,problem.GoalList) 
                    pqueue.add(w,nNode,nActions)
                    visited.append((nNode, len(actions)))
