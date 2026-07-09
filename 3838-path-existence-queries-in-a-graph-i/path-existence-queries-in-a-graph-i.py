class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[py] = px

        # Connect adjacent nodes
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                union(i, i + 1)

        ans = []
        for u, v in queries:
            ans.append(find(u) == find(v))

        return ans