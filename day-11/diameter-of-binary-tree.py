from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def depth(self, node):
        if not node: 
            return 0
        
        L = self.depth(node.left)
        R = self.depth(node.right)
        self.ans = max(self.ans, L+R+1)
        return max(L, R) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        self.depth(root)
        return self.ans - 1
        

def buildTree(node: TreeNode, index: int, items: List[int]) -> TreeNode:
    if len(items) > index:
        node = TreeNode(items[index])
        node.left = buildTree(None, 2*index + 1, items)
        node.right = buildTree(None, 2*index + 2, items)

        return node

    return None


if __name__ == "__main__":
    node = buildTree(None, 0, [1, 2, 3, 4, 5])
    
    solution = Solution()
    print(str(solution.diameterOfBinaryTree(node)))