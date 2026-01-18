class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def check(x, y, k):
            s = row[x][y + k] - row[x][y]
            if diag1[x + k][y + k] - diag1[x][y] != s:
                return False
            if diag2[x + k][y] - diag2[x][y + k] != s:
                return False
            for i in range(k):
                if row[x + i][y + k] - row[x + i][y] != s:
                    return False
                if col[x + k][y + i] - col[x][y + i] != s:
                    return False
            return True

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if check(i, j, k):
                        return k
        return 1
