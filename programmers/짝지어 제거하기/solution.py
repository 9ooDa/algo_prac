// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12973#

def solution(s):
    stack = []
    
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    
    if len(stack) == 0:
        return 1
    else:
        return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     queue = deque(s)
#     ans = 1
    
#     for _ in range(len(s) * 2):
#         if len(queue) == 0:
#             break
            
#         curr = queue.popleft()
        
#         if curr == queue[0]:
#             ans = 1
#             queue.popleft()
#         else:
#             ans = 0
#             queue.append(curr)
    
#     return ans