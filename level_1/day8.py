# 직사각형 별찍기(3번째식이 가장 빠름)
## 1번식
a, b = map(int, input().strip().split(' '))
for _ in range(1, b+1):
    print(a * '*')
## 2번식
a, b = map(int, input().strip().split(' '))
print(('*' * a + '\n') * b)
## 3번식
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)

# 최대공약수와 최소공배수
### 1. math 모듈
from math import gcd
def solution(n, m):
    return [gcd(n,m), n*m/gcd(n,m)]

### 2. for - 최대 공약수, 공배수 구하기
## 최대 공약수 구하기
#### a, b를 모두 나눌 수 있는 약수(공통약수) 중 가장 큰 수
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
## 최소 공배수 구하기
#### 공통 배수들 중 가장 작은 것.
for i in range(max(a, b), (a*b)+1):
    if i % a == 0 and i % b == 0:
        print(i)
        break

### 3. 유클리드 호제법 - 최대공약수, 공배수 구하기
'''
유클리드 호제법 : x, y의 최대공약수는 y, r의 최대 공약수와 같음
               : x를 y로 나눈 나머지값 == r
''' 
## 최대 공약수 구하기
def GCD(x, y) :
    while y : # y가 참일 동안 = 자연수일 때 = a%b !=0 
        x, y = y, x%y
    return x
print(GCD(10, 12))
## 최소 공배수 구하기
def LCM(x, y):
    result = (x*y)//GCD(x, y)
    return result
print(LCM(10, 12))


# 같은 숫자는 싫어(스택/큐)
def solution(arr):
    answer = []
    for elem in arr:
        if len(answer) == 0:
            answer.append(elem)
        ## 연속적이지 않은 숫자 삽입.
        elif elem != answer[-1]:
            answer.append(elem)
    return answer

## 번외(distinct)
def solution(arr):
    answer = list(set(arr))
    return answer

# 이상한 문자 만들기
def solution(s):
    answer = ''
    for i in s.split(' '):
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[:-1]
