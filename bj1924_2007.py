# 11분 통과

import sys

x, y = map(int, sys.stdin.readline().rstrip().split())

days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
remaining_dict = {0:'SUN', 1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT'}
days = y

for i in range(1, x):
    days += days_in_month[i]

print(remaining_dict[days % 7])