# Gabbi Forsythe
# AI Project 3
# 4/20/2020

# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # negative value because the game ends (no living cost)
        if action == "Stop":
            return -100

        # negative value because you die
        for ghostState in newGhostStates:
            if newPos == ghostState.getPosition() and ghostState.scaredTimer == 0:
                return -100

        maxScore = -1000000
        # get the shortest manhattan distance
        for food in currentGameState.getFood().asList():
            score = -1*manhattanDistance(food, newPos)
            if score > maxScore:
                maxScore = score

        return maxScore

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state

        self.evaluationFunction(currentGameState )

        self.depth

        """
        "*** YOUR CODE HERE ***"

        score, action = self.pacmanActions(gameState, self.depth)
        return action


    # this function chooses pacmans actions
    # Return: (score, action)
    def pacmanActions(self, gameState, curDepth):
        # check if the game state is a terminal state, or if the minimax tree has been reached the limit
        if gameState.isWin() or gameState.isLose() or curDepth == 0:
            return (self.evaluationFunction(gameState), "")

        bestScore = -100000000
        bestAction = ""

        # go through all the options that pacman has
        for action in gameState.getLegalActions(0):
            # get the successor state of the action
            successorState= gameState.generateSuccessor(0, action)
            # get the values of the ghostActions 
            successorScore = self.ghostActions(successorState, curDepth, 1)
            if bestScore < successorScore:  # take the max score
                bestScore = successorScore
                bestAction = action
            
        return (bestScore, bestAction)  # return score for use in the ghost function, action for use in the getAction function 

    # this functions determines the ghost(s) actions
    # Returns: score
    def ghostActions(self, gameState, curDepth, ghost):
        # check if the game state is a terminal state, or if the minimax tree has been reached the limit
        if gameState.isWin() or gameState.isLose() or curDepth == 0: 
            return self.evaluationFunction(gameState)

        minScore = 100000000

        for action in gameState.getLegalActions(ghost):
            successorState = gameState.generateSuccessor(ghost, action)

            # the last ghost action should trigger the pacman action in the tree
            if ghost == gameState.getNumAgents() - 1:
                successorScore, action = self.pacmanActions(successorState, curDepth - 1)
            # ghost calls for next ghost action
            else:
                successorScore = self.ghostActions(successorState, curDepth, ghost + 1)

            if minScore > successorScore:
                minScore = successorScore
        
        return minScore

            

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        score, action = self.maxValue(gameState, float("-inf"), float("inf"), self.depth)
        return action
        # util.raiseNotDefined()

    # finds the max node of the tree; same as pacmanAction function from above minimax problem
    def maxValue(self, gameState, alpha, beta, curDepth):
        # check if the game state is a terminal state, or if the minimax tree has been reached the limit
        if gameState.isWin() or gameState.isLose() or curDepth == 0:
            return (self.evaluationFunction(gameState), "")
        
        v = float("-inf")
        vAction = ""

        # go through all the options that pacman has
        for action in gameState.getLegalActions(0):
            # get the successor state of the action
            successorState= gameState.generateSuccessor(0, action)
            # get the values of the ghostActions 
            successorScore = self.minValue(successorState, alpha, beta, curDepth, 1)
            if v < successorScore:  # take the max score
                v = successorScore
                vAction = action
            
            if v > beta:
                return (v, "")
            alpha = max(alpha, v)

        return (v, vAction)  # return score for use in the ghost function, action for use in the getAction function 

    # this functions determines the ghost(s) actions
    # Returns: score
    def minValue(self, gameState, alpha, beta, curDepth, ghost):
        # check if the game state is a terminal state, or if the minimax tree has been reached the limit
        if gameState.isWin() or gameState.isLose() or curDepth == 0: 
            return self.evaluationFunction(gameState)

        v = float("inf")

        for action in gameState.getLegalActions(ghost):
            successorState = gameState.generateSuccessor(ghost, action)

            # the last ghost action should trigger the pacman action in the tree
            if ghost == gameState.getNumAgents() - 1:
                successorScore, action = self.maxValue(successorState, alpha, beta, curDepth - 1)
            # ghost calls for next ghost action
            else:
                successorScore = self.minValue(successorState, alpha, beta, curDepth, ghost + 1)

            if v > successorScore:
                v = successorScore

            if v < alpha:
                return v
            
            beta = min(beta, v)
        
        return v


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
