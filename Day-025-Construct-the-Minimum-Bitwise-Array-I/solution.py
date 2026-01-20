class Solution:
    def minBitwiseArray(self, nums):
        res = []
        for n in nums:
            if n % 2 == 0:
                res.append(-1)
            else:
                k = 0
                t = n
                while t & 1:
                    k += 1
                    t >>= 1
                res.append(n - (1 << (k - 1)))
        return res
