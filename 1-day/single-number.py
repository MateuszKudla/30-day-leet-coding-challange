from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        for number in nums:
            result ^= number
            
        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.singleNumber([2,6,2,5,3,3,5])
    print (result)