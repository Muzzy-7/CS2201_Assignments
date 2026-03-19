# AI Assignment 3 - SEARCH ALGORITHMS

# Contents
1. [Dijkstra / Uniform Cost Search](#Dijkstra-/-Uniform-Cost-Search)
2. [Unmanned Ground Vehicle path planning](#Unmanned-Ground-Vehicle-(UGV)-path-planning-using-A*)
3. [Dynamic UGC path planning](#Dynamic-UGV-Path-Planning-using-A*-Algorithm)

## Dijkstra / Uniform Cost Search

This project implements **Dijkstra’s Algorithm (Uniform Cost Search)** to find the shortest distances between cities using road distances in India.

### Introduction

In a state space where actions have different costs, the best approach is to use **Uniform Cost Search**, also known as **Dijkstra’s Algorithm**.

Here we take:
- Takes a **source city** as input
- Computes **shortest distance to all cities**
- Displays **shortest path to a selected destination**

###  Algorithm Used

Dijkstra’s Algorithm works as follows:

1. Assign distance = infinity to all nodes
2. Set source distance = 0
3. Use a priority queue
4. Always expand the node with the smallest distance
5. Update distances of neighboring nodes
6. Repeat until all nodes are visited

### Input Data

The data is stored in a CSV file: indian_cities_dataset

Example:
Origin, Destination, Distance
Agra, Delhi,240
Agra, Lucknow,334
Each row represents a **road connection between two cities**.


### How It Works

1. The CSV file is read and converted into a **graph (adjacency list)**
2. The user enters:
   - Source city  
   - Destination city  
3. Dijkstra’s algorithm computes:
   - Shortest distances  
   - Parent nodes for path reconstruction  
4. The path is traced from the destination back to the source

###  Output

The program displays:

- Shortest distance from the source to all cities  
- Shortest path from source to destination  

Example:
<img width="496" height="659" alt="image" src="https://github.com/user-attachments/assets/edf34933-7c7e-448a-a91b-07750663ef74" />

## Unmanned Ground Vehicle (UGV) path planning using A*

An Unmanned Ground Vehicle (UGV) must navigate through a battlefield environment while avoiding obstacles and reaching a target location.
This project models the environment as a grid and uses **A\* (A-star) search algorithm** to compute the shortest path.

###  Problem Description

- Grid size: **70 × 70**
- Start and goal positions are **user-defined**
- Obstacles are:
  - Randomly generated

The objective is to:
> Find the **optimal path** from start to goal while avoiding obstacles.

### User Inputs

The user provides:

- Start position `(row, column)`
- Goal position `(row, column)`
- Obstacle density level

### How It Works

1. A grid is created with random obstacles  
2. Start and goal positions are set  
3. A* algorithm is applied:
   - Uses open list (basic list)
   - Selects node with lowest cost
   - Explores neighbors (including diagonals)
4. Builds the shortest path using parent tracking  

### Measures of Effectiveness

The algorithm evaluates performance using:

- **Path Length** → number of nodes in path  
- **Cost** → total movement cost  
- **Nodes Explored** → number of nodes visited  
- **Time Taken** → execution time  

### Output

Example output:

<img width="344" height="456" alt="image" src="https://github.com/user-attachments/assets/c019af8b-1068-441c-8cd0-04062a6d0365" />

### Visualization

The grid is displayed using **matplotlib**
<img width="638" height="638" alt="image" src="https://github.com/user-attachments/assets/e725b12b-a31f-4d3f-8cb9-ca24baaa2c75" />


## Dynamic UGV Path Planning using A* Algorithm

### Introduction

In real-world scenarios, obstacles are not always known beforehand and may change over time. This project simulates such an environment and enables a UGV to navigate safely using **dynamic path planning**.

### Problem Description

- Grid size: **70 × 70**
- Each cell:
  - `0` → free space  
  - `1` → obstacle  
- Obstacles are generated randomly based on density:
  - Low (10%)
  - Medium (25%)
  - High (40%)

The goal is to:
> Navigate from a user-defined start position to a goal position while avoiding obstacles that may appear dynamically.

### Dynamic Environment

Unlike static path planning:

- The UGV **moves step-by-step**
- New obstacles can appear randomly during movement
- The algorithm **replans the path using A*** at every step

This simulates real-world uncertain environments.

### User Inputs

The user provides:

- Start position `(row, column)`
- Goal position `(row, column)`
- Obstacle density level

### How It Works

1. A grid is generated with random obstacles  
2. Start and goal positions are set  
3. The UGV:
   - Plans a path using A*  
   - Moves one step  
   - Checks for new obstacles  
   - Recomputes path if needed  
4. This continues until the goal is reached  

### Measures of Effectiveness

The algorithm is evaluated using:

- **Path Length** → number of steps taken  
- **Cost** → total movement cost  
- **Nodes Explored** → total nodes visited during search  
- **Time Taken** → total execution time  

### Output

Example:
<img width="373" height="409" alt="image" src="https://github.com/user-attachments/assets/48ef97e6-4d57-4050-aa59-33b63b0ed1de" />
<img width="645" height="622" alt="image" src="https://github.com/user-attachments/assets/5642c28a-02b5-42d0-aea9-e64b7c74263a" />




 
