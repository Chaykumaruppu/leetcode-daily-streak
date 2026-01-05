class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        neg = 0
        mn = float('inf')
        
        for row in matrix:
            for x in row:
                total += abs(x)
                if x < 0:
                    neg += 1
                mn = min(mn, abs(x))
        
        return total if neg % 2 == 0 else total - 2 * mn
