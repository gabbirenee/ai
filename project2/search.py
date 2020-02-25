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
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    from util import Stack
    stack = Stack() # the frontier aka the oregon trail
    visited = []    # will hold the list of nodes we have been to
    stack.push((problem.getStartState(), []))
    
    while not(stack.isEmpty()):
        temp = stack.pop()
        current = temp[0]   # current state of the node
        actions = temp[1]   # actions to get to current node
        # print(problem.getSuccessors(current))
        if problem.isGoalState(current):
            print("Goal Found at ", current)
            # print(actions)
            return actions
        else:
            visited.append(current)    # add the node to the list of visited nodes
            for child in problem.getSuccessors(current):
                # print(child)
                childState = child[0]   # coordinates/state of the child node
                childDirect = child[1]  # directions of the child node from the current node (NSEW)
                if childState not in visited:
                    stack.push((childState, actions + [childDirect])) # add the node to the frontier if it is not the goal state
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue() # the frontier aka the oregon trail
    visited = []    # will hold the list of nodes we have been to
    queue.push((problem.getStartState(), []))
    
    while not(queue.isEmpty()):
        temp = queue.pop()
        current = temp[0]   # current state of the node
        actions = temp[1]   # actions to get to current node
        if problem.isGoalState(current):
            print("Goal Found at ", current)
            # print(actions)
            return actions
        else:
            visited.append(current)    # add the node to the list of visited nodes
            for child in problem.getSuccessors(current):
                # print(child)
                childState = child[0]   # coordinates/state of the child node
                childDirect = child[1]  # directions of the child node from the current node (NSEW)
                if childState not in visited:
                    queue.push((childState, actions + [childDirect])) # add the node to the frontier if it is not the goal state
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return aStarSearch(problem, nullHeuristic)  # ucs is just astar with a 0 heuristic -- work smarter not harder
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    pq = PriorityQueue() 
    visited = []
    pq.push( (problem.getStartState(), []), heuristic(problem.getStartState(), problem) )
    visited.append(problem.getStartState())

    while not (pq.isEmpty()):
        temp = pq.pop()
        current = temp[0]   # current state of the node
        actions = temp[1]   # actions to get to current node
        if problem.isGoalState(current):
            print("Goal Found at ", current)
            # print(actions)
            return actions
        if current not in visited:
            visited.append(current)
        for child in problem.getSuccessors(current):
            childState = child[0]   # coordinates/state of the child node
            childDirect = child[1]  # directions of the child node from the current node (NSEW)
            if childState not in visited:
                pq.update((childState, actions + [childDirect]), problem.getCostOfActions(actions + [childDirect])+ heuristic(childState, problem)) # add the node to the frontier if it is not the goal state 
    return []
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
