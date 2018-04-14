#attribution: www.leetcode.com
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isVal(root, mini, maxi): 
            if not root:
                return True
            if root.val >= mini or root.val <= maxi:
                return False

            return isVal(root.left, min(mini, root.val), maxi) and isVal(root.right, mini, max(root.val, maxi))
    
        return isVal(root, float('inf'),float('-inf') )