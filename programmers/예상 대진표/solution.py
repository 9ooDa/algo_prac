// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12985#

def solution(n,a,b):
    def next_rank(x):
        if x % 2 == 0:
            return x // 2
        else:
            return x // 2 + 1
    
    def is_match(x, y):
        if x % 2 == 0:
            if y == x - 1:
                return True
                
        elif x % 2 != 0:
            if y == x + 1:
                return True
        
        return False
    
    match = False
    count = 1
    while True:
        if abs(a - b) == 1:
            if a < b:
                match = is_match(a, b)
            else:
                match = is_match(b, a)
        
        if match == False:
            a = next_rank(a)
            b = next_rank(b)
            count += 1
        else:
            break
    
    return count