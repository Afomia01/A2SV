# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans  = []
        dict = defaultdict(int)
        def traverse(node):
            if node:
                dict[node.val] += 1
                traverse(node.right)
                traverse(node.left)
        traverse(root)

        max_mode = max(dict.values())
        for keys, values in dict.items():
            if values == max_mode:
                ans.append(keys)
        return ans