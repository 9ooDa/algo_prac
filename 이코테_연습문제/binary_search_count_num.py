from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)

    return right_index - left_index


n, x = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

count = count_by_range(n_list, x, x)

if count == 0:
    print(-1)
else:
    print(count)