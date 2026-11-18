class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        ans = 0
        currP = 0

        for right in range(len(prices)):
            currP = prices[right] - prices[left]

            if currP < 0:
                left = right
            else:
                ans = max(ans, currP)

        return ans 