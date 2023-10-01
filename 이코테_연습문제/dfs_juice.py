r, c = map(int, input().split())

tray = []
for i in range(r):
    tray.append(list(map(int, input())))

print(tray)

# 0 -> 얼음
# 1 -> 칸막이

# 매 번 상하좌우를 확인해보고 방문여부확인 (1은 방문 불가 노드)
def dfs(x, y):
    if x <= -1 or x >= r or y <= -1 or y >= c:
        return False
    if tray[x][y] == 0:
        # 방문 처리
        tray[x][y] = 1
        # 상, 하, 좌, 우 호출 (재귀)
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(r):
    for j in range(c):
        if dfs(i, j) == True:
            result += 1

print(result)