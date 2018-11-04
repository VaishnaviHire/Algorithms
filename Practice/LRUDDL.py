class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dct = {}
        self.capacity = capacity

    def addTail(self, node):

        tmpnd = self.tail.prev
        tmpnd.next = node
        node.prev = tmpnd
        node.next = self.tail
        self.tail.prev = node
        # print "AddingTail"+str(node.value)

    def remNode(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        tmpnd = self.tail.prev
        tmpnd.next = node
        node.prev = tmpnd
        node.next = self.tail
        self.tail.prev = node
        # print "REAddingTail"+str(node.value)
        return node

    def removeHead(self):
        hd = self.head.next.key
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return hd

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dct:  # .keys():
            node = self.dct[key]
            self.remNode(node)
            return self.dct[key].value

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dct:  # .keys():
            node = self.dct[key]
            nd = self.remNode(node)
            nd.value = value
            self.dct[key] = nd

        else:
            nd = Node(key, value)
            self.addTail(nd)
            self.dct[key] = nd

            if len(self.dct) > self.capacity:
                # print self.head.next.value
                # print self.dct.keys()
                key = self.removeHead()
                del self.dct[key]
                # print "deleting"+str(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)