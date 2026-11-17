class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            k = (left + right) // 2
            hours_needed = sum((pile + k - 1) // k for pile in piles)

            if hours_needed <= h:
                right = k
            else:
                left = k + 1

        return left