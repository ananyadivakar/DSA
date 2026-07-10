class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        arr.sort()

        pos = [0] * n
        for i in range(n):
            pos[arr[i][1]] = i

        LOG = 1
        while (1 << LOG) < n:
            LOG += 1

        up = [[0] * LOG for _ in range(n)]

        r = 0
        for l in range(n):
            if r < l:
                r = l

            while r + 1 < n and arr[r + 1][0] - arr[l][0] <= maxDiff:
                r += 1

            up[l][0] = r

        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]

        ans = []

        for u, v in queries:
            src = pos[u]
            dest = pos[v]

            if src > dest:
                src, dest = dest, src

            if src == dest:
                ans.append(0)
                continue

            curr = src
            hops = 0

            for j in range(LOG - 1, -1, -1):
                if up[curr][j] < dest:
                    curr = up[curr][j]
                    hops += 1 << j

            if up[curr][0] >= dest:
                ans.append(hops + 1)
            else:
                ans.append(-1)

        return ans