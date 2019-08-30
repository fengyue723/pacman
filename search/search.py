# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    if problem.isGoalState(problem.getStartState()):
      return []
    stack = util.Stack()
    stack.push([problem.getStartState(), None, None])
    used = {}
    
    while not stack.isEmpty():
      node = stack.pop()
      if node[0] not in used:
        used[node[0]] = [node[1], node[2]] #state:[action, father]
        if problem.isGoalState(node[0]):
          res = []
          cur = node[0]
          while used[cur][0] != None:
            res.append(used[cur][0])
            cur = used[cur][1]
          res = res[::-1]
          return res
        for child in problem.getSuccessors(node[0]):
          stack.push([child[0], child[1], node[0]])

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    if problem.isGoalState(problem.getStartState()):
      return []
    queue = util.Queue()
    queue.push([problem.getStartState(), None, None])
    used = {}
    
    while not queue.isEmpty():
      node = queue.pop()
      if node[0] not in used:
        used[node[0]] = [node[1], node[2]] #state:[action, father]
        if problem.isGoalState(node[0]):
          res = []
          cur = node[0]
          while used[cur][0] != None:
            res.append(used[cur][0])
            cur = used[cur][1]
          res = res[::-1]
          return res
        for child in problem.getSuccessors(node[0]):
          queue.push([child[0], child[1], node[0]])
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    heap = util.PriorityQueue()
    heap.push((problem.getStartState(), 0, None, None), 0)
    
    closed = {}
    best_g = {}
    
    while not heap.isEmpty():
      node = heap.pop()
      #for child in problem.getSuccessors(node):
      g = node[1]
      if node[0] not in closed or g < best_g[node[0]]:
        closed[node[0]] = [g, node[2], node[3]] #state:[g,action,father]
        best_g[node[0]] = g

        if problem.isGoalState(node[0]):
          res=[]
          cur=node[0]
          while closed[cur][2] != None:
            res.append(closed[cur][1])
            cur = closed[cur][2]
          res = res[::-1]
          return res

        for child in problem.getSuccessors(node[0]):
          g2 = g + child[2]
          heap.push((child[0], g2, child[1], node[0]), g2)


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE IF YOU WANT TO PRACTICE ***"
    

    heap = util.PriorityQueue()
    h0 = heuristic(problem.getStartState(), problem)
    heap.push((problem.getStartState(), 0, None, None), [h0, h0])
    
    closed = {}
    best_g = {}
    
    while not heap.isEmpty():
      node = heap.pop()
      #for child in problem.getSuccessors(node):
      g = node[1]
      if node[0] not in closed or g < best_g[node[0]]:
        closed[node[0]] = [g, node[2], node[3]] #state:[g,action,father]
        best_g[node[0]] = g

        if problem.isGoalState(node[0]):
          res=[]
          cur=node[0]
          while closed[cur][2] != None:
            res.append(closed[cur][1])
            cur = closed[cur][2]
          res = res[::-1]
          return res

        for child in problem.getSuccessors(node[0]):
          h = heuristic(child[0],problem)
          g2 = g + child[2]
          heap.push((child[0], g2, child[1], node[0]), [g2+h,h])

    util.raiseNotDefined()

def iterativeDeepeningSearch(problem):
    """Search the deepest node in an iterative manner."""
    "*** YOUR CODE HERE FOR TASK 1 ***"
    if problem.isGoalState(problem.getStartState()):
      return []
    depth=1
    while True:
      stack = [[problem.getStartState(),0]]
      used = {problem.getStartState():[None, None, 0]}
      while stack:
        node = stack.pop()
        if node[1] < depth:
          for child in problem.getSuccessors(node[0]):
            if child[0] not in used or used[node[0]][2]+1 < used[child[0]][2]:
              used[child[0]] = [node[0], child[1], used[node[0]][2]+1]
              stack.append([child[0], node[1]+1])
            if problem.isGoalState(child[0]):
              res = []
              cur = child[0]
              while used[cur][0] != None:
                res.append(used[cur][1])
                cur = used[cur][0]
              res = res[::-1]
              return res
      depth += 1

    util.raiseNotDefined()

def waStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has has the weighted (x 2) lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE FOR TASK 2 ***"
    
    heap = util.PriorityQueue()
    h0 = heuristic(problem.getStartState(), problem)
    heap.push((problem.getStartState(), 0, None, None), [2*h0, h0])
    
    closed = {}
    best_g = {}
    
    while not heap.isEmpty():
      node = heap.pop()
      #for child in problem.getSuccessors(node):
      g = node[1]
      if node[0] not in closed or g < best_g[node[0]]:
        closed[node[0]] = [g, node[2], node[3]] #state:[g,action,father]
        best_g[node[0]] = g

        if problem.isGoalState(node[0]):
          res=[]
          cur=node[0]
          while closed[cur][2] != None:
            res.append(closed[cur][1])
            cur = closed[cur][2]
          res = res[::-1]
          return res

        for child in problem.getSuccessors(node[0]):
          h = heuristic(child[0],problem)
          g2 = g + child[2]
          heap.push((child[0], g2, child[1], node[0]), [g2+2*h,h])

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
wastar = waStarSearch
