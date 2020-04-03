from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        answer = 0
        anyPositive = False

        for number in nums:
            if number > 0:
                anyPositive = True

            if maxSum + number > 0:
                maxSum += number
            else:
                maxSum = 0
            
            answer = max(answer, maxSum)

        if not anyPositive:
            return max(nums)

        return answer


if __name__ == "__main__":
    solution = Solution()
    result = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print (result)