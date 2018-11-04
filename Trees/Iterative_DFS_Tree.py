import collections
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder_iterative_dfs(self,root):

        stack =[]
        result = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result

    def preorder_iterative_dfs(self,root):
        stack =[]
        result = []

        while stack or root:
            while root:
                stack.append(root)
                result.append(root.val)
                root = root.left

            root = stack.pop()
            root = root.right
        return result

    def postorder_iterative_dfs(self,root):
        stack = []
        result = []

        while root or stack:
            while root:
                stack.append(root)
                result = [root.val] + result
                root = root.right

            root = stack.pop()
            root = root.left
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

print "Inorder",a.inorder_iterative_dfs(a1)
print "Preorder", a.preorder_iterative_dfs(a1)
print "Postorder", a.postorder_iterative_dfs(a1)


