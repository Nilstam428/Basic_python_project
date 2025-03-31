# Auto-generated Python script - 2025-03-31
# Question: Create a Python implementation of the A* search algorithm

```python
import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic distance to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(maze, start, goal):
    start_node = Node(start)
    goal_node = Node(goal)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        (x, y) = current_node.position

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
            node_position = (x + new_position[0], y + new_position[1])

            if node_position[0] < 0 or node_position[0] >= len(maze) or node_position[1] < 0 or node_position[1] >= len(maze[0]):
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(node_position, current_node)
            new_node.g = current_node.g + 1
            new_node.h = heuristic(goal, new_node.position)
            new_node.f = new_node.g + new_node.h

            if new_node in closed_list:
                continue

            if new_node not in [i for i in open_list]:
                heapq.heappush(open_list, new_node)

    return []
```

# If this code contains a function or class but no execution code,
# here's a simple test to run it:

def test_solution():
    print("Testing the solution...")
    # Add test code here if needed
    print("Test completed!")

if __name__ == "__main__":
    test_solution()
