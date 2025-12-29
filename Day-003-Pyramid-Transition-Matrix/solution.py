class Solution:
    def pyramidTransition(self, bottom, allowed):
        from collections import defaultdict

        mp = defaultdict(list)
        for rule in allowed:
            mp[(rule[0], rule[1])].append(rule[2])

        memo = set()

        def dfs(row):
            if len(row) == 1:
                return True
            if row in memo:
                return False

            def build_next(i, path):
                if i == len(row) - 1:
                    return dfs(path)
                key = (row[i], row[i + 1])
                if key not in mp:
                    return False
                for ch in mp[key]:
                    if build_next(i + 1, path + ch):
                        return True
                return False

            res = build_next(0, "")
            if not res:
                memo.add(row)
            return res

        return dfs(bottom)
