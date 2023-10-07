// [문제 링크]: https://www.acmicpc.net/problem/10816

import sys
from bisect import bisect_left, bisect_right
​
def find_range(arr, x):
    left = bisect_left(arr, x)
    right = bisect_right(arr, x)
    return right - left
​
n = int(sys.stdin.readline().rstrip())
narr = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())
marr = list(map(int, sys.stdin.readline().rstrip().split()))
​
for x in marr:
    print(find_range(narr, x), end=' ')