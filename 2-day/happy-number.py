class Solution:
    def isHappy(self, n: int) -> bool:
        slow  = n
        fast = n
        
        while True:
            slow = self.calculateSquareSum(slow)
            fast = self.calculateSquareSum(self.calculateSquareSum(fast))

            if slow == fast:
                break
            
        return slow == 1


    def calculateSquareSum(self, n: int) -> int:
        squareSum = 0
        while n != 0:
            digit = n % 10
            n //= 10
            squareSum += digit**2

        return squareSum


if __name__ == "__main__":
    solution = Solution()
    result = solution.isHappy(19)
    print (result)
        