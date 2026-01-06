from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        q = deque([root])
        level = 1
        best_level = 1
        best_sum = root.val

        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if s > best_sum:
                best_sum = s
                best_level = level

            level += 1

        return best_level
