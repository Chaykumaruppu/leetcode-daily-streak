class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        
        same = 6
        diff = 6
        
        for _ in range(1, n):
            ns = (same * 3 + diff * 2) % MOD
            nd = (same * 2 + diff * 2) % MOD
            same, diff = ns, nd
        
        return (same + diff) % MOD
