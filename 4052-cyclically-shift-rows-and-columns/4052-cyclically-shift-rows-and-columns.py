class Solution(object):
    def cyclicShift(self, n, grid, rowShift, colShift):
        for i in range(n):
            k = rowShift[i]
            grid[i] = grid[i][k:] + grid[i][:k]

        for j in range(n):
            k = colShift[j]
            col = [grid[i][j] for i in range(n)]
            col = col[k:] + col[:k]

            for i in range(n):
                grid[i][j] = col[i]

        return grid