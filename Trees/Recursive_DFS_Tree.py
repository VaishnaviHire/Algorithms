class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder_recursive_dfs(self,root):
        if not root:
            return
        else:
            return self.inorder_recursive_dfs(root.left) + [root.val] + self.inorder_recursive_dfs(root.right)

    def preorder_recursive_dfs(self,root):
        if not root:
            return
        else:
            return [root.val] + self.preorder_recursive_dfs(root.left) + self.preorder_recursive_dfs(root.right)

    def postorder_recursive_dfs(self,root):
        if not root:
            return
        else:
            return self.preorder_recursive_dfs(root.left) + self.preorder_recursive_dfs(root.right) + [root.val]



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

print "Inorder",a.inorder_recursive_dfs(a1)
print "Preorder", a.preorder_recursive_dfs(a1)
print "Postorder", a.postorder_recursive_dfs(a1)