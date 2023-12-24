// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/68935#

import math

def solution(n):
    max_pow = int(math.log(n, 3))
    base_three = []
    flag = 0
    remain = n
    
    for i in range(max_pow, -1, -1):
        flag = 3 ** i
        if flag * 2 <= remain:
            base_three.append(2)
            remain -= flag * 2
        elif flag <= remain:
            base_three.append(1)
            remain -= flag
        else:
            base_three.append(0)
    
    base_three_flip = base_three[::-1]
    
    base_ten = 0
    j = 0
    for i in range(max_pow, -1, -1):
        base_ten += (3 ** i) * base_three_flip[j]
        j += 1
        
    return base_ten