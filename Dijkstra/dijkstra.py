import csv
import heapq

graph = {}

def add_edge(a, b, d):
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append((b, d))
    graph[b].append((a, d))

def load_file():
    file = open("indian_cities_dataset.csv", "r")
    reader = csv.DictReader(file)

    for row in reader:
        city1 = row["Origin"].strip().lower()
        city2 = row["Destination"].strip().lower()
        dist = float(row["Distance"])

        add_edge(city1, city2, dist)

    file.close()

def dijkstra(start):
    dist = {}
    parent = {}

    for node in graph:
        dist[node] = float("inf")
        parent[node] = None

    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        current_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent

def get_path(parent, end):
    path = []
    while end != None:
        path.append(end)
        end = parent[end]

    path.reverse()
    return path

load_file()

start = input("Enter source city: ").lower()

distances, parent = dijkstra(start)

print("\nShortest distances:\n")
for city in distances:
    print(city, "=", distances[city], "km")

end = input("\nEnter destination city: ").lower()

if end not in distances or distances[end] == float("inf"):
    print("No path found")
else:
    path = get_path(parent, end)
    print("\nPath:")
    print(" -> ".join(path))
    print("Total distance:", distances[end], "km")