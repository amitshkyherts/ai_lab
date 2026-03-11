from pprint import pp

state = ({
    ("hero", 1): "left",
    ("kick", 1): "left",
    ("hero", 2): "left",
    ("kick", 2): "left",
    ("hero", 3): "left",
    ("kick", 3): "left",
}, "left")

pp(state)


def token(state):
    return (tuple(sorted(state[0].items())), state[1])


visited = set()
visited.add(token(state))
visited.add(token(({
    ("hero", 1): "right",
    ("kick", 1): "left",
    ("hero", 2): "left",
    ("kick", 2): "left",
    ("hero", 3): "left",
    ("kick", 3): "left",
}, "left")))
visited.add(token(({
    ("hero", 1): "right",
    ("kick", 1): "right",
    ("hero", 2): "left",
    ("kick", 2): "left",
    ("hero", 3): "left",
    ("kick", 3): "left",
}, "left")))
pp(visited)
