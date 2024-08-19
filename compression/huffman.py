from collections import defaultdict
import heapq

class TrieNode(object):

    def __init__(self, char, freq):

        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.parent = None

    def __lt__(self, other):
        
        return self.freq < other.freq


def construct_huffman_tree(T):

    char_to_freq = defaultdict(lambda: 0)
    char_to_node = defaultdict(lambda: None)
    trie_heap = []

    for c in T:
        char_to_freq[c] += 1

    for (char, freq) in char_to_freq:
        new_node = TrieNode(char, freq)
        heapq.heappush(trie_heap, new_node)
        char_to_node[char] = new_node

    while len(trie_heap) > 1:
        trie_1 = heapq.heappop(trie_heap)
        trie_2 = heapq.heappop(trie_heap)

        parent_node = TrieNode("", trie_1.freq + trie_2.freq)
        parent_node.left = trie_1
        parent_node.right = trie_2

        trie_1.parent = parent_node
        trie_2.parent = parent_node

        heapq.heappush(trie_heap, parent_node)
    
    return heapq.heappop(trie_heap), char_to_node


        
def huffman_encode(S):

    huffman_tree, char_to_node = construct_huffman_tree(S)

    C = ""

    for c in S:

        char_encoded = ""

        curr_node = char_to_node[c]

        while curr_node.parent is not None:
            if curr_node.parent.left == curr_node:
                char_encoded = "0" + char_encoded
            else:
                char_encoded = "1" + char_encoded
            curr_node = curr_node.parent

        C += char_encoded
    
    return C

