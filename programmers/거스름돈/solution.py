// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    
    arr = [1] + [0]*n
    for c in money:
        for i in range(c, n+1):
            arr[i] += arr[i-c]
    return arr.pop()