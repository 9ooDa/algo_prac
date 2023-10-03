def solution(n, computers):

    def dfs(i):
        visited[i] = 1

        for j in range(n):
            if computers[i][j] == 1 and visited[j] == 0:
                dfs(j)

    visited = [0] * n
    count = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            count += 1

    return count

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))