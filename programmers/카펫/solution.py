// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for col in range(1, int(yellow**0.5)+1):
        if yellow % col == 0:
            row = yellow // col
            if (2 * row) + (2 * col) + 4 == brown:
                return [row+2, col+2]