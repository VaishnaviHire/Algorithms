class Doubly(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None


class Answer(object):
    def firstUnique(self,s):
        repeat = [False]*256
        included = [None] * 256

        print ord('')
        head = Doubly(None)
        temp = head
        for i in s:
            if not repeat[ord(i)]:
                if included[ord(i)]:
                    included[ord(i)]
                else:


a = Answer()
a.firstUnique('absdjk')