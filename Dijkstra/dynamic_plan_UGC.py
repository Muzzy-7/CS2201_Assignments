import math
import random
import time
import matplotlib.pyplot as plt

grid_size = 70

def create_grid(density):
    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            if random.random() < density:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid

def get_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar(grid, start, goal):

    open_list = [start]
    came_from = {}

    g = {start: 0}
    f = {start: get_distance(start, goal)}

    visited = 0

    while len(open_list) > 0:

        current = open_list[0]
        for node in open_list:
            if f[node] < f[current]:
                current = node

        visited += 1

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, visited

        open_list.remove(current)

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for d in directions:
            nx = current[0] + d[0]
            ny = current[1] + d[1]
            neighbor = (nx, ny)

            if nx < 0 or nx >= grid_size or ny < 0 or ny >= grid_size:
                continue

            if grid[nx][ny] == 1:
                continue

            new_cost = g[current] + 1

            if neighbor not in g or new_cost < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = new_cost
                f[neighbor] = new_cost + get_distance(neighbor, goal)

                if neighbor not in open_list:
                    open_list.append(neighbor)

    return [], visited

def simulate(grid, start, goal):

    current = start
    full_path = [current]

    total_visited = 0
    start_time = time.time()

    while current != goal:

        path, visited = astar(grid, current, goal)
        total_visited += visited

        if len(path) == 0:
            print("No path found")
            return full_path, total_visited, time.time() - start_time

        next_step = path[1]
        current = next_step
        full_path.append(current)

        if random.random() < 0.1:
            x = random.randint(0, grid_size-1)
            y = random.randint(0, grid_size-1)

            if (x, y) != current and (x, y) != goal:
                grid[x][y] = 1   # new obstacle

    end_time = time.time()
    return full_path, total_visited, end_time - start_time


print("Enter START[0-69]")
sr = int(input("Row: "))
sc = int(input("Col: "))

print("Enter GOAL [0-69]")
gr = int(input("Row: "))
gc = int(input("Col: "))

print("1.Low  2.Medium  3.High")
choice = int(input("Density: "))

if choice == 1:
    density = 0.1
elif choice == 2:
    density = 0.25
else:
    density = 0.4

grid = create_grid(density)

start = (sr, sc)
goal = (gr, gc)

grid[sr][sc] = 0
grid[gr][gc] = 0

print("\nRunning dynamic path planning...")

path, visited, time_taken = simulate(grid, start, goal)

print("\nPath length:", len(path))
print("Cost:", len(path)-1)

print("\nMeasures of Effectiveness")
print("Nodes explored:", visited)
print("Time taken:", round(time_taken, 6), "seconds")

plt.imshow(grid, cmap='Greys')

if len(path) > 0:
    px = []
    py = []
    for p in path:
        px.append(p[1])
        py.append(p[0])
    plt.plot(px, py, color='blue')

plt.scatter(start[1], start[0], color='green', s=100)
plt.scatter(goal[1], goal[0], color='red', s=100)

plt.title("Dynamic UGV Navigation")
plt.show()