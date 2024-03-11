# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checker(self, root, prev):
        if root is not None:
            if not self.checker(root.left, prev):  
                return False

            if prev[0] is not None and root.val <= prev[0].val:  
                return False

            prev[0] = root  
            return self.checker(root.right, prev) 

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [None]  
        return self.checker(root, prev)
   
        