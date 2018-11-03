#
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        temp_head = head

        while temp_head:
            temp_node = RandomListNode(temp_head.label)
            temp_node.next = temp_head.next
            temp_head.next = temp_node
            temp_head =  temp_node.next

        temp_head = head

        while temp_head:
            if temp_head.random:
                temp_head.next.random = temp_head.random.next
            else:
                temp_head.next.random = None
            temp_head = temp_head.next

        ori = head
        new = head.next
        new_head = head.next
        while ori:
            ori.next = ori.next.next
            if new.next:
                new.next = new.next.next
            else:
                new.next = None

            ori = ori.next
            new - new.next

        return new_head





