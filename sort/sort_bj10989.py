n = int(input())

num = []
for _ in range(n):
    num.append(int(input()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    rest = arr[1:]

    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

ans = quick_sort(num)

for i in range(len(ans)):
    print(ans[i])