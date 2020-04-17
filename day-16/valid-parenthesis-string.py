class Solution:
    def checkValidString(self, s: str) -> bool:
        smallestValue = 0
        largestValue = 0
        for char in s:
            smallestValue += 1 if char == '(' else -1
            largestValue += 1 if char != ')' else -1
            if largestValue < 0: break
            smallestValue = max(smallestValue, 0)

        return smallestValue == 0
        

if __name__ == "__main__":
    solution = Solution()
    result = solution.checkValidString("(()())")
    print (result)