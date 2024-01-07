// [문제 링크]: https://www.acmicpc.net/problem/1978

def is_prime(x):
    if x == 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
​
n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    if is_prime(num):
        cnt += 1
​
print(cnt)