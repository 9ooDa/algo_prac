# 시작 위치 (1, 1)
# 출구 (n, m)
# 괴물 o -> 0, x -> 1
# 최소칸의 개수 (시작, 최종 칸 포함)
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        # 제일 처음 위치부터
        x, y = queue.popleft()

        for i in range(4):
            # 현재 위치의 상 하 좌 우 확인
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 몬스터가 있으면 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))