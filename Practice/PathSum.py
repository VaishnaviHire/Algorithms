# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and  not root.left and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        # stack = [root]
        # result = []
        # while stack:
        #     root = stack.pop()
        #     result.append(root.val)
        #
        #     if not root:
        #         return result
        #
        #     if root.right:
        #         stack.append(root.right)
        #     if root.left:
        #         stack.append(root.left)
        #
        #     if not root.right and not root.left:
        #         print result
        #         result.pop()
        #         # print(curr_sum)
        #
        # return result











a = Solution()
a1 = TreeNode(5)
a2 = TreeNode(4)
a3 = TreeNode(8)
a4 = TreeNode(11)
a5 = TreeNode(13)
a6 = TreeNode(4)
a7 = TreeNode(7)
a8 = TreeNode(2)
a9 = TreeNode(1)

a1.left =a2
a1.right = a3
a3.left = a5
a3.right=a6
a2.left=a4
a4.left=a7
a4.right =a8
a6.right = a9

print a.hasPathSum(a1,22)
