def solution(numbers):
    '''
    삽입 정렬 (O(N^2)이라서 시간초과 뜸) --> Merge sort나 quick sort로 풀어야함
    '''
    
    if all(num == 0 for num in numbers):
        return "0"
    
    elif all(num < 10 for num in numbers):
        numbers = sorted(numbers, reverse=True)
        new_num = list(map(str, numbers))
        return ''.join(new_num)
    
    else:
        new_num = list(map(str, numbers))
        for i in range(1, len(new_num)):
            for j in range(i, 0, -1):
                if new_num[j][0] == new_num[j-1][0]:
                    if int(new_num[j]+new_num[j-1]) > int(new_num[j-1]+new_num[j]):
                        new_num[j], new_num[j-1] = new_num[j-1], new_num[j]
                    else:
                        continue
                elif new_num[j][0] > new_num[j-1][0]:
                    new_num[j], new_num[j-1] = new_num[j-1], new_num[j]
                else:
                    continue
                
    return ''.join(new_num)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))