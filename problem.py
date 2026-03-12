class IProblem:
    def start_state(self):
        pass

    def is_goal(self, state):
        pass

    def successor_states(self, state):
        pass

    def token(self, state):
        pass


def dfs(problem: IProblem, node, visited=set()) -> list:
    """
    Depth-first search
    """
    token = problem.token(node)
    if token in visited:
        return None

    # create a new set that contains the node
    visited = visited.union(set([token]))

    if problem.is_goal(node):
        return [node]

    for next_node in problem.successor_states(node):
        solution = dfs(problem, next_node, visited)
        if solution:
            return [node] + solution


def bfs(problem: IProblem, candidates, visited=set()) -> list:
    """
    Breadth-first search
    """
    if not candidates:
        return

    # candidates is a queue
    c = candidates.pop(0)  # pop from the front
    node = c[-1]           # must exist

    token = problem.token(node)
    if token in visited:
        return bfs(problem, candidates, visited)

    visited = visited.union(set([token]))

    if problem.is_goal(node):
        return c

    for next_node in problem.successor_states(node):
        if problem.token(next_node) not in visited:
            candidates.append(c + [next_node])

    return bfs(problem, candidates, visited)
