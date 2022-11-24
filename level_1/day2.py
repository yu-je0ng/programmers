# 자연수 뒤집어 베열로 만들기
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer

# 정수 제곱근 판별
def solution(n):
    answer = 0
    num = n**0.5
    if num == int(num):
        answer = (num+1)**2
    else : 
        answer = -1
    return answer
## isinstance(num, int), test case1 -> num = 11.0, False

# 문자열 내 p와 y의 개수
def solution(s):
    answer = True
    # 대소문자 구분 X
    s = s.lower()
    y = s.count("y")
    p = s.count("p")
    if y == p:
        answer = True
    else :
        answer = False
    return answer

# 문자열을 정수로 바꾸기
def solution(s):
    answer = int(s)
    return answer