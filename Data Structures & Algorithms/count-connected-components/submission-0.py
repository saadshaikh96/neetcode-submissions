class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(list)
        for node, connection in edges:
            connections[node].append(connection)
            connections[connection].append(node)
        
        visited = set()
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                self.dfs(node, connections, visited)

        return components


    def dfs(self, node, connections, visited):
        if node in visited:
            return
        visited.add(node)
        for connection in connections[node]:
            self.dfs(connection, connections, visited)
