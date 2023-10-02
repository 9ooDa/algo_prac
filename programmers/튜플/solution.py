// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s_list = list(map(lambda x: [int(i) for i in x], [x.replace('{', '').replace('}', '').split(',') for x in s.split('},')]))
    
    elems = []
    for sl in sorted(s_list, key=lambda x: len(x)):
        for num in sl:
            if num not in elems:
                elems.append(num)
            
    return elems