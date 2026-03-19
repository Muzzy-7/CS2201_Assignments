import math
import random
import matplotlib.pyplot as plt
import time

grid_size = 70
grid = []

print("Obstacle Density:")
print("1. Low   2. Medium   3. High")
choice = int(input("Choose: "))

if choice == 1:
    density = 0.10
elif choice == 2:
    density = 0.25
else:
    density = 0.40

for i in range(grid_size):
    row = []
    for j in range(grid_size):
        if random.random() < density:
            row.append(1)
        else:
            row.append(0)
    grid.append(row)

print("\nEnter START position (0-69)")
sr = int(input("Row: "))
sc = int(input("Col): "))

print("\nEnter GOAL position (0-69)")
gr = int(input("Row: "))
gc = int(input("Col): "))

start_pos = (sr, sc)
goal_pos = (gr, gc)

grid[sr][sc] = 0
grid[gr][gc] = 0


def get_distance(x1, y1, x2, y2):
    a = (x1 - x2) ** 2
    b = (y1 - y2) ** 2
    return math.sqrt(a + b)

def find_path():
    start_time = time.time()

    open_list = [start_pos]
    
    came_from = {}
    
    g_score = {}
    g_score[start_pos] = 0
    
    f_score = {}
    f_score[start_pos] = get_distance(start_pos[0], start_pos[1], goal_pos[0], goal_pos[1])

    visited = 0
    
    while len(open_list) > 0:
        current = open_list[0]
        lowest_f = f_score[current]
        
        for node in open_list:
            if f_score[node] < lowest_f:
                lowest_f = f_score[node]
                current = node

        visited += 1
                
        if current == goal_pos:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start_pos)
            path.reverse()

            end_time = time.time()
            return path, visited, end_time - start_time
            
        open_list.remove(current)
        
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        for d in directions:
            nx = current[0] + d[0]
            ny = current[1] + d[1]
            neighbor = (nx, ny)
            
            if nx < 0 or nx >= grid_size or ny < 0 or ny >= grid_size:
                continue
                
            if grid[nx][ny] == 1:
                continue
                
            move_cost = 1.0
            if d[0] != 0 and d[1] != 0:
                move_cost = 1.414
                
            new_cost = g_score[current] + move_cost
            
            if neighbor not in g_score or new_cost < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = new_cost
                
                dist_to_goal = get_distance(nx, ny, goal_pos[0], goal_pos[1])
                f_score[neighbor] = new_cost + dist_to_goal
                
                if neighbor not in open_list:
                    open_list.append(neighbor)

    end_time = time.time()
    return [], visited, end_time - start_time

print("\nSearching for a path...")
final_path, visited, time_taken = find_path()

if len(final_path) > 0:
    print("Path found!")
    print("Path length:", len(final_path))
    print("Cost:", len(final_path) - 1)
else:
    print("No path found")

print("\n--- Measures of Effectiveness ---")
print("Nodes explored:", visited)
print("Time taken:", round(time_taken, 6), "seconds")

plt.imshow(grid, cmap='Greys')

if len(final_path) > 0:
    path_x = []
    path_y = []
    for p in final_path:
        path_x.append(p[1])
        path_y.append(p[0])
    plt.plot(path_x, path_y, color='blue', linewidth=2, label='Path')

plt.scatter(start_pos[1], start_pos[0], color='green', s=100, label='Start')
plt.scatter(goal_pos[1], goal_pos[0], color='red', s=100, label='Goal')

plt.title("UGV Navigation")
plt.legend()
plt.show()