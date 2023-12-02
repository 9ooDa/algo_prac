import sys

def solution(m: int, k: int, arr: list):
    arr.sort(reverse=True)
    elem_num = 0
    consec = 0
    res = 0
    while elem_num < m:
        if consec < k:
            res += arr[0]
            consec += 1
            elem_num += 1
        else:
            if arr[0] == arr[1]:
                consec = 0
            else:
                res += arr[1]
                elem_num += 1
                consec = 0
    return res

n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(m, k, arr))