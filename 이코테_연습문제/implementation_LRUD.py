n = int(input())
dir_list = list(map(str, input().split()))
curr_x, curr_y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for dir in dir_list:
    for i in range(len(move_types)):
        if dir == move_types[i]:
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    curr_x, curr_y = nx, ny

print(curr_x, curr_y)