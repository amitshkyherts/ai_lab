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


# ------------- NOT WORKING!!!!! ------------------
def bfs(problem: IProblem, nodes) -> list:
    """
    Breadth-first search
    """
    if not nodes:
        return

    node = nodes.pop(0)  # pop from the front
    n = node[-1]     # must exist

    if problem.is_goal(n):
        return node

    for next_node in problem.successor_states(n):
        nodes.append(node + [next_node])

    return bfs(problem, nodes)
