from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")  # Process the current node
                visited.add(node)
                if node in self.graph:
                    # Push unvisited neighbors onto the stack
                    stack.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")  # Process the current node
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Traversal (starting from vertex 2):")
g.dfs(2)


print("\nBreadth-First Traversal (starting from vertex 2):")
g.bfs(2)