n = int(input())

coord = []
for _ in range(n):
    coord.append(list(map(int, input().split())))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    rest = arr[1:]

    left = []
    right = []
    for c in rest:
        if c[0] < pivot[0]:
            left.append(c)
        elif c[0] > pivot[0]:
            right.append(c)
        else:
            if c[1] < pivot[1]:
                left.append(c)
            elif c[1] > pivot[1]:
                right.append(c)

    return quick_sort(left) + [pivot] + quick_sort(right)

ans = quick_sort(sorted(coord))
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])

# ans = sorted(coord, key=lambda x: (x[0], (x[1])))

# for x in ans:
#     print(x[0], x[1])
