def successors(state):
    empty = state.index('E')
    # generate a list of candidate positions
    candidates = [empty-2, empty-1, empty+1, empty+2]
    # keep only valid indices
    candidates = [c for c in candidates if c >= 0 and c < len(state)]
    candidates = [
        c  # think of this as the current animal
        for c in candidates
        if state[c:c+2] == ['C', 'E']  # if c is swapable with the next element
        or state[c-1:c+1] == ['E', 'S']  # swapable with prev el
        or state[c:c+3] == ['C', 'S', 'E']  # swapable with second el after
        or state[c-2:c+1] == ['E', 'C', 'S']  # swapable with second el before
    ]

    for c in candidates:
        state_copy = state.copy()
        # swap with empty
        state_copy[c], state_copy[empty] = state_copy[empty], state_copy[c]
        yield state_copy


def solution(state, goal_state):
    if state == goal_state:
        return [state]

    for next_state in successors(state):
        sol = solution(next_state, goal_state)
        if sol:
            return [state] + sol


def main():
    state = ['C', 'C', 'E', 'S', 'S']
    goal_state = ['S', 'S', 'E', 'C', 'C']

    for s in solution(state, goal_state):
        print(s)


if __name__ == "__main__":
    main()
