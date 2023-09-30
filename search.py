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


# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS
# - Akhil Arularasu

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
    stack = util.Stack()
    visited = []

    start_state = problem.getStartState()
    print('start:', start_state)
    path = []
    stack.push((start_state, path))
    visited.append(start_state)  # Mark the start state as visited

    print("Is the start a goal?", problem.isGoalState(start_state))
    print("Start's successors:", problem.getSuccessors(start_state))

    while not stack.isEmpty():
        current_state, current_path = stack.pop()

        if problem.isGoalState(current_state):
            return current_path

        for successor in problem.getSuccessors(current_state):
            successorState, action, stepCost = successor
            if successorState not in visited:
                visited.append(successorState)
                new_path = current_path + [action]  # Append neighbor to the path
                stack.push((successorState, new_path))

# getSuccessor returns a list of triples, (successor,
 #       action, stepCost), where 'successor' is a successor to the current
 #       state, 'action' is the action required to get there, and 'stepCost' is
 #       the incremental cost of expanding to that successor.
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited = []

    start_state = problem.getStartState()
    print('start:', start_state)
    path = []
    queue.push((start_state, path))
    visited.append(start_state)  # Mark the start state as visited

    while not queue.isEmpty():
        current_state, current_path = queue.pop()

        if problem.isGoalState(current_state):
            return current_path
        
        for successor in problem.getSuccessors(current_state):
            successorState, action, stepCost = successor
            if successorState not in visited:
                visited.append(successorState)
                new_path = current_path + [action]  # Append neighbor to the path
                queue.push((successorState, new_path))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    pq = util.PriorityQueue()
    visited = []

    start_state = problem.getStartState()
    print('start:', start_state)
    path = []
    pq.push((start_state, path), 0)
    visited.append(start_state)  # Mark the start state as visited
    while not pq.isEmpty():
        current_state, current_path = pq.pop()

        if problem.isGoalState(current_state):
            return current_path  # Return the path if the goal state is reached
        
        for next_state, action, step_cost in problem.getSuccessors(current_state):
            if next_state not in visited:
                visited.append(next_state)  # Mark the next state as visited
                next_path = current_path + [action]
                total_cost = problem.getCostOfActions(next_path)
                pq.push((next_state, next_path), total_cost)  # Push the next state and path with the total cost

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    visited = []

    start_state = problem.getStartState()
    print('start:', start_state)
    path = []
    pq.push((start_state, path), 0)
    visited.append(start_state)  # Mark the start state as visited
    
    while not pq.isEmpty():
        current_state, current_path = pq.pop()

        if problem.isGoalState(current_state):
            return current_path  # Return the path if the goal state is reached
        
        for next_state, action, step_cost in problem.getSuccessors(current_state):
            if next_state not in visited:
                visited.append(next_state)  # Mark the next state as visited
                next_path = current_path + [action] 
                g_cost = problem.getCostOfActions(next_path)  # Cost to reach next state
                h_cost = heuristic(next_state, problem)  # Heuristic cost to reach the goal from next state
                total_cost = g_cost + h_cost  # Combined cost
                pq.push((next_state, next_path), total_cost)  # Push the next state and path with the combined cost
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
