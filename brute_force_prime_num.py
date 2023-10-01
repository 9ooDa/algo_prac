def solution(numbers):
    def is_prime_num(number):
        prime = []
        for i in range(2, number+1):
            divisible = False
            for j in range(2, i):
                if i % j == 0:
                    divisible = True
            if divisible == False:
                prime.append(i)
        return prime
        
    piece = [*numbers]
    max_num = int((lambda x: ''.join(x))(sorted([*numbers], reverse=True)))
    prime_list = list(map(str, is_prime_num(max_num)))
    print(piece)
    
    for prime in prime_list:
        if all(x in prime for x in piece):
            print(prime)
    
    