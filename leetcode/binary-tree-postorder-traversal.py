# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        left= self.postorderTraversal(root.left)
        right= self.postorderTraversal(root.right)
        ans=[]
        ans.extend(left)
        ans.extend(right)
        ans.append(root.val)
        return ans
        