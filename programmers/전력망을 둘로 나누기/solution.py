// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def solution(n, wires):
    def bfs(x):
        queue = deque([x])
        visited = [0] * (n + 1)
        visited[x] = 1
        count = 1
        while queue:
            curr = queue.popleft()

            for i in graph[curr]:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)
                    count += 1
        return count
    
    graph = [[] for _ in range(n+1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    res = n
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        res = min(abs(bfs(v1) - bfs(v2)), res)

        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return res