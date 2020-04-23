from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {}
        map[0] = 1
        count, sum = 0, 0

        for num in nums:
            sum += num
            if sum - k in map:
                count += map[sum - k]

            if sum in map:
                map[sum] = map[sum] + 1
            else:
                map[sum] = 1

        return count



if __name__ == "__main__":
    solution = Solution()
    result = solution.subarraySum([1,1,1], 2)
    print (result)
        