from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {}
        map[0] = -1
        maxlen = 0
        count = 0

        for index in range(0, len(nums)):
            count += nums[index] if nums[index] == 1 else -1
            if count in map:
                maxlen = max(maxlen, index - map[count])
            else:
                map[count] = index
        
        return maxlen


if __name__ == "__main__":
    solution = Solution()
    result = solution.findMaxLength([0,1,0,0,1,1,0])
    print (result)