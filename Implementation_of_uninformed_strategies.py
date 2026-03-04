def get_next_states(x, y, capA, capB):
    states = []
    states.append((capA, y))
    states.append((x, capB))
    states.append((0, y))
    states.append((x, 0))
    pour = min(x, capB - y)
    states.append((x - pour, y + pour))
    pour = min(y, capA - x)
    states.append((x + pour, y - pour))
    return states

# BFS Implementation
def bfs(capA, capB, goal):
    visited = set()
    queue = []
    queue.append((0, 0))
    visited.add((0, 0))
    print("\nBFS Traversal:")

    while queue:
        x, y = queue.pop(0)
        print((x, y))
        if x == goal or y == goal:
            print("Goal Reached:", (x, y))
            return
        for state in get_next_states(x, y, capA, capB):
            if state not in visited:
                visited.add(state)
                queue.append(state)
    print("No Solution Found")

# DFS Implementation
def dfs(capA, capB, goal):
    visited = set()
    stack = [(0, 0)]
    print("\nDFS Traversal:")
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print((x, y))

        if x == goal or y == goal:
            print("Goal Reached:", (x, y))
            return
        for state in get_next_states(x, y, capA, capB):
            if state not in visited:
                stack.append(state)
    print("No Solution Found")

# Depth Limited Search
def dls(capA, capB, goal, limit):
    stack = [((0, 0), 0)]
    visited = set()
    print("\nDLS Traversal (limit =", limit, "):")
    while stack:
        (x, y), depth = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print((x, y), "Depth:", depth)
        if x == goal or y == goal:
            print("Goal Reached:", (x, y))
            return True
        if depth < limit:
            for state in get_next_states(x, y, capA, capB):
                stack.append((state, depth + 1))
    print("Goal not found within depth limit")
    return False

# Iterative Deepening DFS
def iddfs(capA, capB, goal, max_depth):
    print("\nIDDFS Search:")
    for depth in range(max_depth + 1):
        print("\nTrying depth limit:", depth)
        if dls(capA, capB, goal, depth):
            print("Solution found at depth", depth)
            return
    print("Goal not found")
capA = 4
capB = 3
goal = 2

print("Water Jug Problem")
print("Jug A Capacity:", capA)
print("Jug B Capacity:", capB)
print("Goal:", goal)
bfs(capA, capB, goal)
dfs(capA, capB, goal)
dls(capA, capB, goal, 5)

iddfs(capA, capB, goal, 10)
