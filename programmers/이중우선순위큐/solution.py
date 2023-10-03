// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    queue = []
    for operation in operations:
        command, number = operation.split()
        number = int(number)
        
        if command == 'I':
            queue.append(number)
        elif command == 'D' and len(queue) != 0:
            if number == 1:
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
        
    if len(queue) == 0:
        return [0,0]
    else:
        return max(queue), min(queue)