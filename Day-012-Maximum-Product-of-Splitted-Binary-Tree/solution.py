class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.subtree_sums = []

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = node.val + left + right
            self.subtree_sums.append(s)
            return s

        total_sum = dfs(root)
        max_product = 0

        for s in self.subtree_sums:
            max_product = max(max_product, s * (total_sum - s))

        return max_product % MOD
