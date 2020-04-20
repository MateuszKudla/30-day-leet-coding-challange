from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.root = TreeNode(preorder[0])
        
        def bst(item, root):
            if root is None:
                root =  TreeNode(item)
            else:
                if item < root.val:
                    root.left =  bst(item, root.left)
                elif item > root.val:
                    root.right =   bst(item, root.right)
            return root
           
      
        for i in range(1,len(preorder)):
            bst(preorder[i], self.root)

        return self.root

if __name__ == "__main__":
    solution = Solution()
    result = solution.bstFromPreorder([8,5,1,7,10,12])
    print (result)
        