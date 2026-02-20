class Problem:
    def start(self):
        pass

    def is_goal(self, state):
        pass

    def successor_states(self, state):
        pass

    def token(self, state):
        pass


def dfs(problem: Problem, node, visited=set()) -> list:
    """
    Depth-first search
    """
    token = problem.token(node)
    if token in visited:
        return None

    visited = visited.union(set([token]))

    if problem.is_goal(node):
        return [node]

    for next_node in problem.successor_states(node):
        solution = dfs(problem, next_node, visited)
        if solution:
            return [node] + solution
