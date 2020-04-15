from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        answer[0] = 1
        for index in range(1, len(nums)):
            answer[index] = nums[index - 1] * answer[index -1]

        R = 1
        for index in reversed(range(len(nums))):
            answer[index] = answer[index] * R
            R *= nums[index]

        return answer
        
if __name__ == "__main__":
    solution = Solution()
    result = solution.productExceptSelf([1,2,3,4])
    print (result)