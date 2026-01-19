class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

        def get_sum(x1, y1, x2, y2):
            return ps[x2][y2] - ps[x1][y2] - ps[x2][y1] + ps[x1][y1]

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            found = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if get_sum(i, j, i + mid, j + mid) <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                lo = mid
            else:
                hi = mid - 1
        return lo
