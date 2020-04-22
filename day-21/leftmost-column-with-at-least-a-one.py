from typing import List

class BinaryMatrix(object):

    def __init__(self, data: List[List[int]]):
        self.data = data

    def get(self, x: int, y: int) -> int:
        return self.data[x][y]

    def dimensions(self) -> List[int]:
        return [len(self.data), len(self.data[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        pointerN, pointerM = 0, m - 1
        result = -1
        
        while (pointerN < n and pointerM >= 0):
            if binaryMatrix.get(pointerN, pointerM) == 1:
                result = pointerM
                
                pointerM -= 1
            else:
                pointerN += 1
            
        return result


if __name__ == "__main__":
    solution = Solution()
    binaryMartix = BinaryMatrix([[0,0],[0,1]])
    result = solution.leftMostColumnWithOne(binaryMartix)
    print (result)
        
        