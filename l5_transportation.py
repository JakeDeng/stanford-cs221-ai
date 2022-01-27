#Model
#define the search problem => modeling
class TransportationProblem(object):
    def __init__(self, N):
        #N = number of blocks
        self.N = N
    def startState(self):
        return 1;
    def isEnd(self, state):
        return state == self.N
    def succAndCost(self, state):
        #return a list of (action newState, cost) tuples based on the current state
        results = []
        if state+1 <= self.N:
            results.append(('walk', state+1, 1))
        if state*2 <= self.N:
            results.append(('tram', state*2, 2))
        return results
    
#Algorithms
#backtracking Search function using closure 
def backtrackingSearch(problem):
    #best solution variable as the free state variable for the recurse functions
    best = {
        'cost': float('+inf'),
        'history': None
    }
    def recurse(state, history, totalCost):
        #At state, having undergone history, accumulated totalCost 
        #Explore the rest of the subtree
        if problem.isEnd(state):
            #update the best solution so far
            if totalCost < best['cost']:
                best['cost'] = totalCost
                best['history'] = history
            return
        #Recurse on children
            for action, newState, cost in problem.succAndCost(state):
                recurse()
            
    #initial call to start the recursion
    recurse(problem.startState(), history = [], totalCost = 0)
    return (best['cost'], best['history'], best['totalCost'])

def run():
    problem = TransportationProblem(N=10)
    print(problem.succAndCost(3))