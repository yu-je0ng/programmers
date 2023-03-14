# 다음 큰 숫자
'''
자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
'''

def solution(n):
    answer = n
    one_cnt = bin(n).count("1") # n의 2진수의 1의 갯수
    
    while True:
        answer += 1 # 조건1
        answer_cnt = bin(answer).count("1")
        if answer_cnt == one_cnt : # 조건2
            break
    return answer