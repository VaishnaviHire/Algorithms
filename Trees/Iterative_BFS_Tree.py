class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def iterative_bfs(self,root):

        queue = [root]
        result = []

        while queue:

            root = queue.pop(0)

            if root.left :
                queue.append(root.left)
            if root.right:
                queue.append(root.right)


            result.append(root.val)
        return result

a =  Solution()
a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)

a1.left = a2
a1.right = a3
a3.right = a6
a2.left = a4
a2.right =a5

print a.iterative_bfs(a1)