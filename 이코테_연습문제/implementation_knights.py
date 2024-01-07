curr = input()

cols = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
rows = [1, 2, 3, 4, 5, 6, 7, 8]

x, y = int(curr[1]), cols[curr[0]]
cnt = 0

if x - 2 in rows:
    if y - 1 in cols.values():
        cnt += 1
    if y + 1 in cols.values():
        cnt += 1
if x + 2 in rows:
    if y - 1 in cols.values():
        cnt += 1
    if y + 1 in cols.values():
        cnt += 1
if y - 2 in cols.values():
    if x - 1 in rows:
        cnt += 1
    if x + 1 in rows:
        cnt += 1
if y + 2 in cols.values():
    if x - 1 in rows:
        cnt += 1
    if x + 1 in rows:
        cnt += 1

print(cnt)

'''
# 정답 예시
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
'''