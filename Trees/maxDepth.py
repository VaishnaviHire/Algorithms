#attribution: www.leetcode.com

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        else:
            left_height = 1 + self.maxDepth(root.left)
            right_height = 1 + self.maxDepth(root.right)
        
            if left_height > right_height:
                return left_height
            else:
                return right_height
