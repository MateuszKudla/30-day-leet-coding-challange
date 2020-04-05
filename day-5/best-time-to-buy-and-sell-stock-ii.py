from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        
        return maxProfit


if __name__ == "__main__":
    solution = Solution()
    result = solution.maxProfit([7,1,5,3,6,4])
    print (result)