class Solution(object):
    def sumFourDivisors(self, nums):
        total = 0

        for num in nums:
            s = 0
            count = 0
            d = 1

            while d * d <= num:
                if num % d == 0:
                    other = num // d
                    count += 1
                    s += d
                    if other != d:
                        count += 1
                        s += other
                if count > 4:
                    break
                d += 1

            if count == 4:
                total += s

        return total
