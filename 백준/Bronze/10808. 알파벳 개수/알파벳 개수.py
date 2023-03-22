import collections
from string import ascii_lowercase

s=input()
counter=collections.Counter(s)
alphabet_list = list(ascii_lowercase)
for char in alphabet_list:
    print(counter.get(char,0),end=' ')