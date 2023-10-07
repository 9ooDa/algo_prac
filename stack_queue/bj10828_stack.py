'''
통과
5분
'''
import sys

n = int(sys.stdin.readline().rstrip())

arr = [sys.stdin.readline().rstrip().split() for _ in range(n)]

stack = []

for l in arr:
    if l[0] == 'push':
        stack.append(int(l[1]))
    
    elif l[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif l[0] == 'size':
        print(len(stack))

    elif l[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    
    elif l[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)