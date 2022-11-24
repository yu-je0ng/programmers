# 모든문제>안 푼 문제>난이도1>Python3>정답률 높은 순 정렬

# 짝수와 홀수
def solution(num):
    answer = ''
    if num%2 == 0 : answer = "Even"
    else : answer = "Odd"
    return answer

# 약수의 합
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0 :
            answer += i 
    return answer

# 평균 구하기
def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

# 자릿수 더하기.
def solution(n):
    answer = 0
    n = list(str(n))
    for i in n :
        answer += int(i)
    return answer