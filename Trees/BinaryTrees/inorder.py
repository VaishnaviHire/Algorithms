
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left =None
        self.right = None

class Traversal:
    def recursive_inorder(self, root):
        if not root:
            return []

        return self.recursive_inorder(root.left) + [root.val] + self.recursive_inorder(root.right)


    def iterative_inorder(self,root):

        res = []
        queue = []

        if not root:
            return res

        while True:

            while root:
                queue.append(root)
                root = root.left

            if not queue:
                return res
            root = queue.pop()
            if root:
                res.append(root.val)

            root = root.right

    def bfs(self,root):
        queue = [root]
        res = []

        while queue:

            curr = queue.pop(0)

            if curr:
                res.append(curr.val)
                queue.append(curr.left)

                queue.append(curr.right)

        return res

def main():
    a = Traversal()
    root = TreeNode(9)
    n2 = TreeNode(10)
    n3 = TreeNode(2)
    n4 = TreeNode(1)
    n5 = TreeNode(3)

    root.left = n2
    root.right = n3
    n2.left = n4
    n2.right = n5

    print(a.recursive_inorder(root))
    print(a.iterative_inorder(root))
    print(a.bfs(root))

if __name__ == "__main__":
    main()