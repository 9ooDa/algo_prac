import sys

def solution(n, m, arr):
    row2num = {}
    row = 1
    for i in range(0, len(arr), m):
        row2num[row] = arr[i:i+m]
        row += 1
    
    res = -1
    for _, v in row2num.items():
        res = max(min(v), res)

    return res


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []

for _ in range(n):
    graph.extend(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(n, m, graph))