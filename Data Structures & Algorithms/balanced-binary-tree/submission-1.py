# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return [True , 0]
            leftChild,rightChild = dfs(curr.left),dfs(curr.right)
            balanced = leftChild[0] and rightChild[0] and abs(leftChild[1] - rightChild[1]) <= 1
            return [balanced, max(leftChild[1],rightChild[1]) + 1]
        return dfs(root)[0]
