class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections = defaultdict(list)
        for u, v, w in times:
            connections[u].append((v, w))

        times = {node: float("inf") for node in range(1, n +1)}

        self.dfs(k, 0, times, connections)

        delayTime = max(times.values())
        return delayTime if delayTime != float("inf") else -1

    def dfs(self, node, currentTime, times, connections):
        if currentTime >= times[node]:
            return

        times[node] = currentTime
        for neighbor, time in connections[node]:
            self.dfs(neighbor, currentTime + time, times, connections)