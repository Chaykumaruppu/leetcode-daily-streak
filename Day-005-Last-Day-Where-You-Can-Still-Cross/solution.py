class Solution:
    def latestDayToCross(self, row, col, cells):
        from collections import deque

        def can_cross(day):
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1  # water

            q = deque()
            visited = [[False] * col for _ in range(row)]

            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    visited[0][j] = True

            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if not visited[nr][nc] and grid[nr][nc] == 0:
                            visited[nr][nc] = True
                            q.append((nr, nc))

            return False

        left, right = 0, row * col
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
