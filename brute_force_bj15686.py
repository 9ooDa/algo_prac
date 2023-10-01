from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        # 현재 위치 = 무조건 집
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or nx > n or ny < 0 or ny > n:
                return

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                
            if graph[nx][ny] == 2:
                graph[nx-1][ny-1]
                queue.append((nx, ny))



n, m = map(int, input().split())
graph = list(map(lambda x: [int(i) for i in x], [input().split() for _ in range(n)]))

print(graph)

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             bfs(i, j)