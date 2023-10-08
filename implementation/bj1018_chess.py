import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
res = []

# 8x8 체스판이기때문에 인덱스 에러를 얻지 않으려면 -7
for i in range(n - 7):
    for j in range(m - 7):
        w_idx = 0 # 흰으로 시작
        b_idx = 0 # 검으로 시작

        for a in range(i, i+8): # 시작지점
            for b in range(j, j+8): # 시작지점
                if (a + b) % 2 == 0: # 위치가 짝수인 경우
                    if board[a][b] != 'B':
                        w_idx += 1 # w로 칠하기
                    if board[a][b] != 'W':
                        b_idx += 1 # b로 칠하기

                else: # 위치가 홀수인 경우
                    if board[a][b] != 'W':
                        w_idx += 1
                    if board[a][b] != 'B':
                        b_idx += 1

        res.append(w_idx) # w로 시작할 때의 칠하는 경우의 수
        res.append(b_idx) # b로 시작할 때의 칠하는 경우의 수

print(min(res))