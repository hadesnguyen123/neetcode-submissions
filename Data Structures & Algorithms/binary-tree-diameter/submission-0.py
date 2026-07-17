# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # calculate the height 
        def dfs(root):
            if not root:
                return 0
            maxleft = dfs(root.left)
            maxright = dfs(root.right)
            self.res = max(self.res, maxleft + maxright)

            return max(maxleft, maxright) + 1

        dfs(root)
        return self.res 