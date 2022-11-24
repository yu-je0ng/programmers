# 하샤드 수
def solution(x):
    answer = True
    num = 0
    for i in str(x):
        num += int(i)
    if x % num == 0 : 
        answer = True
    else :
        answer = False
    return answer

# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = [x]
    y = x
    while len(answer) != n :
        y += x
        answer.append(y)
    return answer

# 정수 내림차순으로 배치하기
def solution(n):
    answer = int(''.join(sorted([num for num in str(n)], reverse=True)))
    return answer


# 나머지가 1이 되는 수 찾기
def solution(n):
    num = 1
    while n % num != 1:
        num += 1
    return num