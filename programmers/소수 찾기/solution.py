// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
def solution(numbers):
    def is_prime_num(number):
        if number <= 1:
            return False
        
        for j in range(2, number):
            if number % j == 0:
                return False
        return True
        
    perm = []
    count = 0
    for i in range(1, len(numbers)+1):
        perm.extend(list(map(lambda x: int(''.join(x)), permutations(numbers, i))))
    
    for p in set(perm):
        if is_prime_num(p):
            count += 1
    
    return count
    
    
    