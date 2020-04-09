class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.changeString(s) == self.changeString(t)

    def changeString(self, s: str) -> str:
        result = ""
        skip = 0
        for char in reversed(s):
            if char == "#":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                result += char

        return result
        

if __name__ == "__main__":
    solution = Solution()
    result = solution.backspaceCompare("a#b#c", "a##c")
    print (result)