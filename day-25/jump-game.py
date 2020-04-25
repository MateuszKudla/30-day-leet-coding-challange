from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]

        for i in range(1, len(nums)):
            if jump == 0:
                return False

            if i + jump > len(nums) - 1:
                break

            jump = max(jump - 1, nums[i])

        return True


if __name__ == "__main__":
    solution = Solution()
    print (solution.canJump([2,3,1,1,4]))