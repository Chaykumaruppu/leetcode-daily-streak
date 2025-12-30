class Solution:
    def numMagicSquaresInside(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0

        def is_magic(r, c):
            if grid[r+1][c+1] != 5:
                return False

            nums = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
                    nums.add(grid[i][j])
            if len(nums) != 9:
                return False

            s = 15
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != s:
                    return False
                if sum(grid[r+k][c+i] for k in range(3)) != s:
                    return False

            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False

            return True

        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic(i, j):
                    count += 1

        return count
