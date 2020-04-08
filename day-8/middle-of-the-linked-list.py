from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        isSlowMove = True
        while fast.next != None:
            if isSlowMove:
                slow = slow.next

            fast = fast.next
            isSlowMove = not isSlowMove

        return slow


def listToListNode(numbers: List[int]) -> ListNode:
    if len(numbers) == 0:
        return None

    head = ListNode(numbers[0])
    head.next = listToListNode(numbers[1:])

    return head

if __name__ == "__main__":
    head = listToListNode([1,2,3,4,5])
    
    solution = Solution()
    result = solution.middleNode(head)
    print (result.val)