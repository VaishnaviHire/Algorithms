# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
#
# Yes
from collections import defaultdict
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = defaultdict(list)

    def insert(self, word):
        if word not in self.trie:
            self.trie[word[0]].append(word)

    def search(self,word):
        if word in self.trie[word[0]]:
            return True
        else:
            return False

    def startsWith(self,prefix):
        for i in self.trie[prefix[0]]:
            if i.startswith(prefix):
                return True
        return False

tr = Trie()
tr.insert("apple")
print tr.search("apple")
print tr.search("app")
print tr.startsWith("ve")
tr.insert("app")
print tr.search("app")