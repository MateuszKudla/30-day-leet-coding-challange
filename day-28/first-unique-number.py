from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = []
        self.dictionary = {}
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        while len(self.queue) > 0 and self.dictionary[self.queue[0]] > 1:
            self.queue.pop(0)
            
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]
        

    def add(self, value: int) -> None:
        if value in self.dictionary:
            self.dictionary[value] += 1
        else:
            self.dictionary[value] = 1
            self.queue.append(value)
        

if __name__ == "__main__":
    firstUnique = FirstUnique([2,3,5])
    print(firstUnique.showFirstUnique())
    firstUnique.add(5)
    print(firstUnique.showFirstUnique())
    firstUnique.add(2)
    print(firstUnique.showFirstUnique())
    firstUnique.add(3)
    print(firstUnique.showFirstUnique())