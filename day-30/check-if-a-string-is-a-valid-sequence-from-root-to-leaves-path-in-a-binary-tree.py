from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root is None:
            return len(arr) == 0

        return self.isValid(root, arr, 0)

    def isValid(self, root: TreeNode, arr: List[int], index: int) -> bool:
        if root.val != arr[index]:
            return False

        if index == len(arr) - 1:
            return root.left is None and root.right is None

        return ((root.left is not None and self.isValid(root.left, arr, index + 1)) or
            (root.right is not None and self.isValid(root.right, arr, index + 1)))
        

def buildTree(node: TreeNode, index: int, items: List[int]) -> TreeNode:
    if len(items) > index:
        if items[index] is not None:
            node = TreeNode(items[index])
            node.left = buildTree(None, 2*index + 1, items)
            node.right = buildTree(None, 2*index + 2, items)

            return node

    return None


if __name__ == "__main__":
    solution = Solution()
    root = buildTree(None, 0, [0,1,0,0,1,0,None,None,1,0,0])
    result = solution.isValidSequence(root, [0,1,0,1])
    print (result)