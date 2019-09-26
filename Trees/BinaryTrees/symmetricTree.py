# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        return self.subtreeReflections(root, root)

    def subtreeReflections(self, t1, t2):

        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        else:
            return (t1.val == t2.val) and (self.subtreeReflections(t1.right, t2.left)) and (
                self.subtreeReflections(t1.left, t2.right))

    # time complexity :  O(n)
    # space complexity : O(n) in worst case height of the tree is O(n)

    # iterative solution

    def isSymmetricIterative(self, root):

        queue = [root, root]

        while queue:

            t1 = queue.pop()
            t2 = queue.pop()

            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

        return True
