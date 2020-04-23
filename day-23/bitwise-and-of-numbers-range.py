import math

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        top = int(math.log(n,2))
        bottom = int(math.log(m,2))
        if top != bottom:
            return 0

        result = m
        for i in range(m + 1, n + 1):
            result = result & i
            
        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.rangeBitwiseAnd(2,5)
    print (result)