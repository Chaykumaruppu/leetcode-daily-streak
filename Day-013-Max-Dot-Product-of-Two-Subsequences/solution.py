class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        # dp[i][j] = max dot product using nums1[:i] and nums2[:j]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prod = nums1[i - 1] * nums2[j - 1]

                dp[i][j] = max(
                    prod,                      # start new subsequence
                    dp[i - 1][j - 1] + prod,   # extend subsequence
                    dp[i - 1][j],              # skip nums1[i-1]
                    dp[i][j - 1]               # skip nums2[j-1]
                )

        return dp[n][m]
