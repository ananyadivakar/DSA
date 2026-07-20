class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        arr = []
        for row in grid:
            arr.extend(row)

        total = len(arr)
        k %= total

        arr = arr[-k:] + arr[:-k]

        idx = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = arr[idx]
                idx += 1

        return grid