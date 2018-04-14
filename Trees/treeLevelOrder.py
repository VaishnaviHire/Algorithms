#attribution: www.leetcode.com
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q1 = []
        q2 = []
        q1.append(root)
        result = []
        if root!= None:
            res1 = [root.val]
            res2 = []

            while(len(q1)> 0 or len(q2)> 0): 
                if res1!= []:
                    result.append(res1)
                while(len(q1)>0):
                    curr_node = q1.pop(0)

                    if curr_node.left:
                        q2.append(curr_node.left)
                        res2.append(curr_node.left.val)

                    if curr_node.right:
                        q2.append(curr_node.right)
                        res2.append(curr_node.right.val)

                res1 = []
                if res2 != []:
                    result.append(res2)

                while (len(q2) > 0):
                    curr_node = q2.pop(0)


                    if curr_node.left:
                        q1.append(curr_node.left)
                        res1.append(curr_node.left.val)

                    if curr_node.right:
                        q1.append(curr_node.right)
                        res1.append(curr_node.right.val)

                res2 =[]
            return result[:len(result)]
        
        else:
            return []