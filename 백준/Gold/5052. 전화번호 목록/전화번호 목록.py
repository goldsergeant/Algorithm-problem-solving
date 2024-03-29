import collections
import sys


class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self,string):
        cur=self.head
        for char in string:
            if char not in cur.children:
                cur.children[char]=Node(char)
            cur=cur.children[char]

    def search(self,string):
        cur=self.head
        for char in string:
            if char in cur.children:
                cur=cur.children[char]
            else:
                return False
        return True

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    numbers = list(sys.stdin.readline().rstrip() for _ in range(N))
    numbers.sort(key=len, reverse=True)
    trie=Trie()
    answer = 'YES'

    for number in numbers:
        if trie.search(number):
            answer='NO'
            break
        else:
            trie.insert(number)

    print(answer)