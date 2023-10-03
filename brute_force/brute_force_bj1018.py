'''
체스판 다시 칠하기 (못 품)
'''
def dfs(x, y):
    return


n, m = map(int, input().split())
board = [input().split() for _ in range(n)]
print(board)

if all(x == 8 for x in [n, m]):
    graph = board
else:
    for i in range(n - 8):
        for j in range(m - 8):
            graph = [c[j:j+8] for c in board[i:i+8]]

print(graph)

