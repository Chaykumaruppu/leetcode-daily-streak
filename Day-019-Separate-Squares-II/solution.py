class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        self.covered_count = [0] * (4 * self.n)
        self.covered_width = [0] * (4 * self.n)

    def add(self, ql, qr, val):
        self._add(0, 0, self.n - 1, ql, qr, val)

    def _add(self, idx, lo, hi, ql, qr, val):
        if qr <= self.xs[lo] or self.xs[hi + 1] <= ql:
            return

        if ql <= self.xs[lo] and self.xs[hi + 1] <= qr:
            self.covered_count[idx] += val
        else:
            mid = (lo + hi) // 2
            self._add(idx * 2 + 1, lo, mid, ql, qr, val)
            self._add(idx * 2 + 2, mid + 1, hi, ql, qr, val)

        if self.covered_count[idx] > 0:
            self.covered_width[idx] = self.xs[hi + 1] - self.xs[lo]
        elif lo == hi:
            self.covered_width[idx] = 0
        else:
            self.covered_width[idx] = (
                self.covered_width[idx * 2 + 1] +
                self.covered_width[idx * 2 + 2]
            )

    def get_covered_width(self):
        return self.covered_width[0]


class Solution:
    def separateSquares(self, squares):
        events = []  # (y, delta, xl, xr)
        xs = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        events.sort()
        xs = sorted(xs)

        def get_total_area():
            tree = SegmentTree(xs)
            area = 0
            prev_y = events[0][0]

            for y, delta, xl, xr in events:
                area += tree.get_covered_width() * (y - prev_y)
                tree.add(xl, xr, delta)
                prev_y = y

            return area

        half_area = get_total_area() / 2.0

        tree = SegmentTree(xs)
        curr_area = 0
        prev_y = events[0][0]

        for y, delta, xl, xr in events:
            width = tree.get_covered_width()
            gain = width * (y - prev_y)

            if curr_area + gain >= half_area:
                return prev_y + (half_area - curr_area) / width

            curr_area += gain
            tree.add(xl, xr, delta)
            prev_y = y

        return -1.0  
