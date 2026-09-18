class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connections = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in edges:
            connections[u].append(v)
            connections[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        queue = deque()
        for i in range(1, len(edges) + 1):
            if indegree[i] == 1:
                queue.append(i)

        while queue:
            node = queue.popleft()
            indegree[node] -= 1
            for neighboringNode in connections[node]:
                indegree[neighboringNode] -= 1
                if indegree[neighboringNode] == 1:
                    queue.append(neighboringNode)

        for u,v in reversed(edges):
            if indegree[u] == 2 and indegree[v] > 0:
                return [u,v]

        return []
        