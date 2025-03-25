import collections
import sys

sys.setrecursionlimit(1000000)
answer = 0


class Node(object):
    def __init__(self, key, is_end=False):
        self.key = key  # 생략가능?
        self.is_end = is_end
        self.children = collections.defaultdict(list)
        self.possible_words_cnt=0


class Trie(object):
    def __init__(self):
        self.head = Node('HEAD')

    def insert(self, string):
        curr_node = self.head

        for char in string:
            # 현재 노드에 해당하는 글자의 자식이 없다면 추가
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 다음 노드로 이동
            curr_node = curr_node.children[char]
        # 반복 종료 후 단어의 끝 표시
        curr_node.is_end = True

    def search(self,node:Node):
        global answer,possible_words
        possible_words_cnt=0
        for child_char,child_node in node.children.items():
            possible_words_cnt+=self.search(child_node)
        if node.is_end:
            possible_words_cnt+=1
        node.possible_words_cnt=possible_words_cnt

        return possible_words_cnt

def print_node_possible_words_cnt(node:Node):
    # print(f'node : {node.key} possible_words_cnt : {node.possible_words_cnt}')
    for child_char,child_node in node.children.items():
        print_node_possible_words_cnt(child_node)

def get_keyboard_cnt(node:Node,word,idx):
    global answer
    if node.possible_words_cnt==1 or idx==len(word)-1:
        return
    get_keyboard_cnt(node.children[word[idx+1]],word,idx+1)
    answer+=1



def solution(words):
    global answer
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)

    trie.search(trie.head)

    for word in words:
        get_keyboard_cnt(trie.head,word,-1)
    return answer

print(solution(	["go", "gone", "guild"]))
print(solution(	["word", "war", "warrior", "world"]))