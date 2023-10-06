def solution(n, arr):
    d = [0] * 100

    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + arr[i]) # 1번 창고만 터는 거랑 0번 + 현재창고 터는 거 중에 max (arr[i] = 현재 창고의 식량 수)

    print(d[n - 1])

solution(4, [1, 3, 1, 5])