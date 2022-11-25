# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        answer += i
    return answer
## 스터디원 한줄 코드
def solution(a, b):
    return sum(num for num in range(min(a, b), max(a, b)+1))


# 콜라츠 추축
def solution(num):
    cnt = 0
    while cnt < 500 and num != 1:
        cnt += 1
        if num % 2 == 0:
            num = num//2
        else:
            num = num*3 + 1

    if num == 1:
        return cnt
    else : 
        return -1

# 서울에서 김서방 찾기
def solution(seoul):
    answer = f'김서방은 {seoul.index("Kim")}에 있다'
    return answer
    
# 핸드폰 번호 가리기
def solution(phone_number):
    answer = (len(phone_number) - 4 )*"*" + phone_number[-4:]
    return answer
