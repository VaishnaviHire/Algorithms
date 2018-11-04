# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# Example:
#
# Given the following perfect binary tree,
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# After calling your function, the tree should look like:
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            q1 = [root]
            q2 = []

            while q1 or q2 :
                while q1:
                    curr = q1.pop(0)
                    if q1 and curr:
                        curr.next = q1[0]
                    if curr:
                        q2.append(curr.left)
                        q2.append(curr.right)


                while q2:
                    curr = q2.pop(0)
                    if q2 and curr:
                        curr.next = q2[0]
                    if curr:
                        q1.append(curr.left)
                        q1.append(curr.right)

a  = Solution()
a1 = TreeLinkNode(1)
a2 = TreeLinkNode(2)
a3 = TreeLinkNode(3)
a4 = TreeLinkNode(4)
a5 = TreeLinkNode(5)
a6 = TreeLinkNode(6)
a7 = TreeLinkNode(7)

root = a1

a1.left = a2
a1.right = a3
a2.left = a4
a2.right = a5
a3.left = a6
a3.right = a7
a.connect(root)
# def preorder(root1):
#
#     if not root1:
#         return []
#
#     return [root1.next.val] + preorder(root1.left) + preorder(root1.right)

print (a1.right.next.val)


