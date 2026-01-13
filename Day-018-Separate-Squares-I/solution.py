class Solution(object):
    def separateSquares(self, squares):
        def area_diff(y):
            above = 0.0
            below = 0.0

            for _, bottom, side in squares:
                top = bottom + side
                area = side * side

                if y <= bottom:
                    above += area
                elif y >= top:
                    below += area
                else:
                    above += (top - y) * side
                    below += (y - bottom) * side

            return above - below

        low = min(y for _, y, _ in squares)
        high = max(y + s for _, y, s in squares)

        for _ in range(80):  # enough for 1e-6 precision
            mid = (low + high) / 2.0
            if area_diff(mid) > 0:
                low = mid
            else:
                high = mid

        return low
