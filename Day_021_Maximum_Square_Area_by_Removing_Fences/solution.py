class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])

        max_side = 0

        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                side = v[j] - v[i]
                if side in h_gaps:
                    max_side = max(max_side, side)

        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD
