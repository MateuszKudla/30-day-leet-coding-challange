from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')

        def caltulateSum(root):
            if root is None:
                return 0
            else:
                leftSum = max(caltulateSum(root.left), 0)
                rightSum = max(caltulateSum(root.right), 0)
                self.max = max(self.max, leftSum + rightSum + root.val)
                return max(leftSum, rightSum, 0) + root.val
        
        caltulateSum(root)
        return self.max


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
    root = buildTree(None, 0, [-10,9,20,None,None,15,7])
    result = solution.maxPathSum(root)
    print (result)
        