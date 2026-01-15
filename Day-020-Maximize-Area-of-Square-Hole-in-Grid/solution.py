class Solution:
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):

        def max_consecutive_gap(bars):
            if not bars:
                return 0
            bars.sort()
            max_gap = 1
            curr = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                else:
                    max_gap = max(max_gap, curr)
                    curr = 1
            return max(max_gap, curr)

        max_h = max_consecutive_gap(hBars)
        max_v = max_consecutive_gap(vBars)

        side = min(max_h + 1, max_v + 1)
        return side * side
