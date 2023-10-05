// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    # for i in range(len(phone_book)-1):
        # if phone_book[i] == phone_book[j][:len(phone_book[i])]:
        #     print(phone_book[j])
        #     print(phone_book[j][:len(phone_book)])
        #     return False
    # return True
    phone_book = sorted(phone_book)
    ans = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            ans = False
    return ans