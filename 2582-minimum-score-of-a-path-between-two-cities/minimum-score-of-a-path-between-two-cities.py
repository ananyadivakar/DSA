from collections import defaultdict, deque

class Solution:
    def minScore(self, n, roads):
        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set([1])
        queue = deque([1])
        ans = float('inf')

        while queue:
            node = queue.popleft()

            for nei, dist in graph[node]:
                ans = min(ans, dist)
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return ans