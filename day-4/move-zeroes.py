from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[lastZero] = nums[lastZero], nums[i]
                lastZero += 1


if __name__ == "__main__":
    array = [0,1,0,3,12]
    solution = Solution()
    solution.moveZeroes(array)
    print (array)