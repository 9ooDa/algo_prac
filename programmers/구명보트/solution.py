// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    queue = deque(sorted(people, reverse=True))
    count = 0
    
    while len(queue) > 1:
        if queue[0] + queue[-1] <= limit:
            queue.pop()
            queue.popleft()
            count += 1
        else:
            count += 1
            queue.popleft()
            
    if len(queue) == 1:
        count += 1
            
    return count
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     def dfs(i, weight):
#         print(people[i])
#         visited[i] = 1
        
#         for j in range(len(people)):
#             if visited[j] == 0 and weight + people[j] <= limit:
#                 dfs(j, weight + people[j])
                
#     visited = [0] * len(people)
#     weight = 0
#     count = 0
#     for i in range(len(people)):
#         if visited[i] == 0:
#             weight += people[i]
#             dfs(i, weight)
#             count += 1
#             weight = 0
            
#     return count
            