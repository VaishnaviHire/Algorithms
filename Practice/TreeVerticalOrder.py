# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples 1:
#
# Input: [3,9,20,null,null,15,7]
#
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
#
# Output:
#
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self,root,height):
        if root:
            return self.inorder(root.left,height+1) + [(root,height)] + self.inorder(root.right,height+1)
        else:
            return []
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        j = 1
        res = []
        ino = self.inorder(root,0)
        temp = []
        temp2 = []
        for i in range(ino):
            if j < len(ino):
                if ino[j][0].left == ino[i][0] or ino[j][0].right == ino[i][0] or ino[i][0].left == ino[j][0] or ino[i][0].right == ino[j][0]:
                    temp.append(ino[i])
                    j+=1

                    for k in range(len(temp)-1):
                        if temp[k][0] > temp[k+1][0]:
                            kk = temp[k+1]
                            temp[k+1] = temp[k]
                            temp[k] == kk
                    for l in temp:
                        temp2.append(l[1].val)

                    res.append(temp2)
                    temp = []
                    temp2 = []
                else:
                    temp.append(ino[i])
                    j+=1

        return  res

