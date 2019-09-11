# Trie

A trie is a data structure used to retrieve strings. It has wide applications in the fields of information retrieval, predictive text , autocomplete etc.

Trie uses the concept of prefixes. A prefix of a string is any substring from 0 to n where n <= len(String).
Trie is used to represent strings and its prefixes as a tree. Each node in this tree can have 26 child nodes representing the english alphabet

For example, if I have to represent three strings as trie, 

string1 = "data"
string2 = "database"
string3 = "datagram"

<img>

As you can see in the diagram, strings are represented in a bottom up way. Trie data structure makes search more efficient.
It creates a separate node for every new character. However, traversing a string doesnt require knowledge of the entire vocabulary.

## General Complexities

The trie is an efficient data structure. We do not need to traverse entire tree to search a word. Hence the time complexity for the word search, insertion is
<b>O(n)</b> where n is the length of the word.

The space complexity however, is quite large. Every node can have at most alphabet-sized nodes. The space complexity is given by <b>O(length_of_longest_word * number_of_keys * alphabet_size)</b>.


## Representation

```
class Node:  
    def __init__(self): 
        self.children = [None] * alphabet_size
        self.end = False      # end of word
```

  