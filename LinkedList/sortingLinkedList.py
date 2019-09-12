# Sort a linkedlist using merge sort.

class ListNode:

    def __init__(self, data):
        self.val = data
        self.next = None

class Solution:


    def insert_front(self, head, value):
        temp = head
        head = ListNode(value)
        head.next = temp

        return head

    def printList(self, head):

        while head:
            print(head.val, end=" ")
            head = head.next


    # function to compare and merge nodes
    def merge(self, left, right):
        res = ""
        if not left:
            res = right

        elif not right:
            res = left

        elif left.val >= right.val:
            res = right
            res.next = self.merge(left, right.next)

        elif right.val >= left.val:
            res = left
            res.next = self.merge(right, left.next)

        return res


    def mergeSort(self, head):

        if not head or not head.next:
            return head

        left, right = self.divide_in_half(head)

        left_sorted = self.mergeSort(left)

        right_sorted = self.mergeSort(right)

        return self.merge(left_sorted, right_sorted)

    def divide_in_half(self, head):

        if not head or not head.next:
            return head, None
        else:
            slow = fast = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next

        left = head
        right = slow.next
        slow.next = None

        return left, right





a = ListNode(3)

sol = Solution()
curr_head = sol.insert_front(a, 5)
curr_head = sol.insert_front(curr_head,93)
curr_head = sol.insert_front(curr_head, 1)
curr_head = sol.insert_front(curr_head, 22)
print("Unsorted List: ", end=" ")
sol.printList(curr_head)
print()
print("Sorted List: ", end=" ")
curr_head = sol.mergeSort(curr_head)
sol.printList(curr_head)

