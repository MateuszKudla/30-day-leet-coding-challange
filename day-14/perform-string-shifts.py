from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shiftValue = 0
        direction = 1

        for item in shift:
            if item[0] == 0:
                shiftValue += item[1]
            else:
                shiftValue -= item[1]

        if shiftValue < 0:
            direction = -1
            shiftValue = -shiftValue

        while shiftValue > len(s):
            shiftValue -= len(s)

        return s[direction * shiftValue:] + s[:direction * shiftValue]

if __name__ == "__main__":
    solution = Solution()
    result = solution.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]])
    print (result)