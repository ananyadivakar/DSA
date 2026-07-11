class Solution:
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                nodes = []
                dfs(i)

                degree_sum = 0
                for node in nodes:
                    degree_sum += len(graph[node])

                k = len(nodes)

                if degree_sum == k * (k - 1):
                    ans += 1

        return ans