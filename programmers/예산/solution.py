// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d = sorted(d)
    total = 0
    count = 0
    for x in d:
        if total == budget:
            break
        if total + x <= budget:
            total += x
            count += 1
        
    return count