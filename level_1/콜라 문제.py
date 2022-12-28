# 콜라 문제
## try01. 성공
## 0.00ms~0.41ms
def solution(a, b, n):
    answer = 0
    while n >= a:
        get = (n // a) * b
        lost = a * (n // a)
        answer += get
        n = n + get - lost
    return answer
