// [문제 링크]: https://www.acmicpc.net/problem/10988

def flip_text(x):
    temp = ''
​
    for i in range(len(x)-1, -1, -1):
        temp = temp + x[i]
​
    return temp
​
import sys
​
s = sys.stdin.readline().rstrip()
l = len(s)
mid = l // 2
​
if l % 2 != 0:
    left = s[:mid]
    right = s[mid+1:]
else:
    left = s[:mid]
    right = s[mid:]
​
flipped_left = flip_text(left)
​
if flipped_left == right:
    print(1)
else:
    print(0)