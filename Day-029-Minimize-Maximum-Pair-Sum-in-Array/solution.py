class Solution:
    def minPairSum(self, nums):
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        return ans
