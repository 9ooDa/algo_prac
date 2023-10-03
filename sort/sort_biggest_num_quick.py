def solution(numbers):
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr)//2]
        arr.pop(len(arr)//2)
        rest = arr
        
        left = []
        right = []
        for x in arr:
            if int(x[0]) > int(pivot[0]):
                left.append(x)
            elif int(x[0]) < int(pivot[0]):
                right.append(x)
            elif int(x[0]) == int(pivot[0]):
                if int(x+pivot) > int(pivot+x):
                    left.append(x)
                else:
                    right.append(x)
        
        return quick_sort(left) + [pivot] + quick_sort(right)
    
    new_num = sorted(list(map(str, numbers)), key=lambda x: x[0], reverse=True)
    if all(num == 0 for num in numbers):
        return "0"
    
    elif all(num < 10 for num in numbers):
        return ''.join(new_num)
    
    else:
        result = quick_sort(new_num)
    return ''.join(result)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))