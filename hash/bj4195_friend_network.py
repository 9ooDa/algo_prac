'''
틀림 - 검색 후 유니온파인드 따라함
'''
from sys import stdin

def find(x):
    if parent[x] != x:
        p = find(parent[x])
        parent[x] = p
        return p
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        number[a] += number[b]
    print(number[a])

tc = int(stdin.readline().rstrip())

for _ in range(tc):
    num = int(stdin.readline().rstrip())
    parent, number = {}, {}
    
    for i in range(num):
        a, b = stdin.readline().rstrip().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
