from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        dic = {}
        for item in arr:
            if item in dic.keys():
                dic[item] += 1
            else:
                dic[item] = 1

        result = 0
        for key, value in dic.items():
            if key + 1 in dic.keys():
                result += value

        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.countElements([1,2,3])
    print (result)