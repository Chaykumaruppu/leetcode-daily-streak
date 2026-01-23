import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        left = [-1] + list(range(n - 1))
        right = list(range(1, n)) + [n]
        alive = [True] * n

        def is_bad(i):
            j = right[i]
            return j < n and nums[i] > nums[j]

        bad = sum(is_bad(i) for i in range(n))

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while bad > 0:
            s, i = heapq.heappop(heap)
            j = right[i]

            if j >= n or not alive[i] or not alive[j]:
                continue
            if nums[i] + nums[j] != s:
                continue

            ops += 1

            if left[i] != -1 and is_bad(left[i]):
                bad -= 1
            if is_bad(i):
                bad -= 1
            if is_bad(j):
                bad -= 1

            nums[i] += nums[j]
            alive[j] = False

            rj = right[j]
            right[i] = rj
            if rj < n:
                left[rj] = i

            if left[i] != -1:
                heapq.heappush(heap, (nums[left[i]] + nums[i], left[i]))
                if is_bad(left[i]):
                    bad += 1

            if rj < n:
                heapq.heappush(heap, (nums[i] + nums[rj], i))
                if is_bad(i):
                    bad += 1

        return ops
