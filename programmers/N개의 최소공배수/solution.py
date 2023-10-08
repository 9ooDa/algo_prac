// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    def gcd(x, y):
        new_x = y
        new_y = x % y
        if new_y == 0:
            return y
        return gcd(new_x, new_y)
            
    def lcm(x, y):
        return (x * y) // gcd(x, y)
    
    arr = sorted(arr)
    flag = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            flag = max(flag, lcm(arr[j], arr[i]))
            arr[i], arr[j] = flag, flag
    return flag