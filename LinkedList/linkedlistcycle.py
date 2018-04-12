# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        try:
            fast_pointer = head.next
            slow_pointer = head

            while fast_pointer is not slow_pointer:
              
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            return True
        except:
            return False
     