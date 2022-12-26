# [1차] 다트 게임
'''
문제 정리
1. 총 3번의 기회.
2. 각 기회 마다 0 ~ 10점 획득 가능.
3. 점수 영역 존재.
- S : single : 점수 **1
- D : Double : 점수 **2
- T : Triple : 점수 **3
- * : 스타상 : 해당 점수와 바로 직전에 받은 점수를 각각 2배
- # : 아차상 : 해당 점수 마이너스
    - 스타상과 아차상은 중첩될 수 있음.
'''
## try01. 성공 
## 전체 탐색 : 속도 빠름.
def solution(dartResult):
    num = ''
    score = []
    for char in dartResult:
        if char.isnumeric():
            num += char
        elif char == "S":
            num = int(num)**1
            score.append(num)
            num = ''
        elif char == "D":
            num = int(num)**2
            score.append(num)
            num = ''
        elif char == "T":
            num = int(num)**3
            score.append(num)
            num = ''
        elif char == "*":
            if len(score) == 1:
                score[-1] = score[-1] * 2
            else :
                score[-1] = score[-1] * 2
                score[-2] = score[-2] * 2
        elif char == "#":
            score[-1] = score[-1] * -1
    return sum(score)

'''
## 문자열이 숫자로 되어있는지 검사하는 함수
# isdecimal(), isdigit(), isnumeric()

# case1
a = '123456789'
print(a.isdigit())
print(a.isdecimal())
print(a.isnumeric())
>>> True
>>> True
>>> True

# case2
b = '5²'
print(b.isdigit())
print(b.isdecimal())
print(b.isnumeric())
>>> True
>>> False
>>> True

# case3 
c = '½'
print(c.isdigit())
print(c.isdecimal())
print(c.isnumeric())
>>> False
>>> False
>>> True


# reson
! 5²에1서 ²는 특수문자
! ½는 그 자체가 특수문자

- isdigit함수는 단일 글자가 '숫자'모양으로 생겼으면 무조건 True를 반환함.
    - 숫자처럼 생긴 모든 글자는 숫자로 인정함.
- isdecimal함수는 주어진 문자열이 int형으로 변환 가능한지 알아내는 함수.
    - 해당 문자열이 0 ~ 9까지 수로 이루어진 것인지 검사
    - 특수문자 중 숫자모양을 숫자로 판단하지 않음.
- isnumeric()함수는 숫자값 표현에 해당하는 문자열까지 인정.
    - 제곲근 및 분수, 거듭제곱 특수문자도 isnumeric()함수는 True를 반환함.
'''

## try02. 성공
## 정규표현식 사용 : try01보다 느림.

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = 0
    return answer
'''
정규표현식 : re
1. re.compile : 정규식 패턴을 정규식 객체로 컴파일함.
    - match(), search(), findall()및 기타 매서드를 일치시키는데 사용됨.
2. re.findall : 문자열 또는 튜플의 목록으로 문자열에서 패턴의 겹치지 않는 모든 일치 항목을 반환함.
    - 문자열은 왼쪽에서 오른쪽으로 스캔되며 찾은 순서대로 일치 항목이 반환함.
    - 빈 일치 항목이 결과에 포함됨.
=========================================================================
1. pattern = re.compile('(\d+)([SDT])([*#]?)')
1-1. print(pattern)
    - re.compile('(\d+)([SDT])([*#]?)')
        - () : (메타문자)일련의 패턴 요소들을 하나의 요소로 묶음.
        - [] : (메타문자)문자클래스
            - [abc]d는 ad, bd, cd를 뜻함.
            - "[a-z]"는 a부터 z까지 중 하나, "[1-9]"는 1부터 9까지 중의 하나를 의미
        - \d+ : (\d)[0-9]숫자 (+)1번 이상 발생.
        - [SDT] 
        - [*#]? : (?)0번또는 1번 발생.

2. dart = pattern.findall(dartResult)
2-1. print(dart)
    - [('1', 'D', ''), ('2', 'S', ''), ('3', 'T', '*')]
2-2. print(re.findall(pattern, dartResult))
    - [('1', 'D', ''), ('2', 'S', ''), ('3', 'T', '*')]
'''