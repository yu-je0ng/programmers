# 숫자 짝꿍
'''
두 정수 X, Y
1. X = 3403이고 Y = 13203이라면, 
    X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330
2. X = 5525이고 Y = 1255이면 
    X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552
3. X, Y의 짝꿍이 존재하지 않으면,
    짝꿍은 -1
'''

## try01. 실패
'''
TypeError: sequence item 0: expected str instance, int found
join할 때는 string이 들어가야 하나 int가 들어가서 발생하는 에러
'''
def solution(X, Y):
    answer = []
    X = list(X)
    Y = list(Y)
    num_min = min(X,Y)
    num_max = max(X,Y)
    for num in num_min:
        if num in num_max:
            answer.append(int(num))
            num_max.remove(num)
            
    if not answer:
        return "-1"
    else:
        return "".join(map(str,sorted(answer, reverse=True)))

## try02. 실패
'''
try01의 오류를 map함수를 사용해서 해결함.
또 다른 문제 answer이 0으로만 구성되어 있을 경우 생각하지 못함.
'''
def solution(X, Y):
    answer = []
    X = list(X)
    Y = list(Y)
    num_min = min(X,Y)
    num_max = max(X,Y)
    for num in num_min:
        if num in num_max:
            answer.append(int(num))
            num_max.remove(num)
            
    if not answer:
        return "-1"
    else:
        return "".join(map(str,sorted(answer, reverse=True)))

## try03. 실패 
## 테스트 11 ~ 15 시간초과
'''
힌트1.
- 반복문으로 모든 숫자를 확인하고 있음.
힌트2.
- 효율적으로 반복되는 문자열 더하기.
    - for _ in range(iternum):
        answer = ''.join([answer, k])
    - answer = ''.join([answer, k*iternum])
    - 두번째방식이 시간 소모에 효율적임.
'''
def solution(X, Y):
    answer = []
    X = list(X)
    Y = list(Y)
    num_min = min(X,Y)
    num_max = max(X,Y)
    for num in num_min:
        if num in num_max:
            answer.append(int(num))
            num_max.remove(num)
    if not answer:
        return "-1"
    elif sum(answer) == 0:
        return "0"
    else:
        return "".join(map(str,sorted(answer, reverse=True)))

## try04. 성공
## dictonary 사용을 고려.
### 시간초과 발생시 항상 dict 사용을 고려해보자.
'''
테스트 11 〉	통과 (505.82ms, 27.4MB)
테스트 12 〉	통과 (519.80ms, 26.7MB)
테스트 13 〉	통과 (505.54ms, 27.5MB)
테스트 14 〉	통과 (534.70ms, 26.7MB)
테스트 15 〉	통과 (491.20ms, 27MB)
'''
def solution(X, Y):
    answer = ''
    
    num_x = {str(n):0 for n in range(10)}
    num_y = {str(n):0 for n in range(10)}

    for x in X:
        num_x[x] += 1
    for y in Y:
        num_y[y] += 1

    for num in range(9, -1, -1): # sort 미사용 가능.
        num = str(num)
        iternum = min(num_x[num], num_y[num]) # 공통적으로 반복된 숫자의 횟수 구하기.
        answer = ''.join([answer, num*iternum]) # 기존값(answer)과 새로운 짝꿍값(num*iternum) 

    if answer == '':
        return "-1"
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer

## try05. 성공
## Counter함수를 사용해서 dictonary 생성: - for문을 줄여줌.
'''
테스트 11 〉	통과 (374.02ms, 53.4MB)
테스트 12 〉	통과 (374.07ms, 51.2MB)
테스트 13 〉	통과 (360.66ms, 53.5MB)
테스트 14 〉	통과 (410.29ms, 51.2MB)
테스트 15 〉	통과 (354.30ms, 46.6MB)
'''
from collections import Counter
def solution(X, Y):
    X, Y = Counter(X), Counter(Y)
    common = ''
    for num in X.keys():
        if num in Y.keys():
            common += num * min(X[num], Y[num])
    if common:
        if common.count("0") == len(common):
            return "0"
        else:
            return ''.join(sorted(common, reverse=True))
    else:
        return "-1"
'''
Counter함수
def solution(X, Y):
    X, Y = Counter(X), Counter(Y)
    return X, Y

>>> solution("100", "2345")
(Counter({'0': 2, '1': 1}), Counter({'2': 1, '3': 1, '4': 1, '5': 1}))
'''

## try06. 성공
## 성능 높이기 : try04, 05 조합
'''
테스트 11 〉	통과 (266.73ms, 27.3MB)
테스트 12 〉	통과 (268.69ms, 26.7MB)
테스트 13 〉	통과 (304.95ms, 27.5MB)
테스트 14 〉	통과 (239.39ms, 26.6MB)
테스트 15 〉	통과 (285.19ms, 26.9MB)
'''
from collections import Counter
def solution(X, Y):
    X, Y = Counter(X), Counter(Y)
    answer = ''
    for num in range(9, -1, -1): # sort 미사용 가능.
        num = str(num)
        iternum = min(X[num], Y[num]) 
        answer = ''.join([answer, num*iternum])
    if answer == '':
        return "-1"
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer

## try07. 
## 추천 답안
'''
테스트 11 〉	통과 (80.79ms, 27.6MB)
테스트 12 〉	통과 (81.11ms, 27.7MB)
테스트 13 〉	통과 (81.57ms, 27.6MB)
테스트 14 〉	통과 (80.97ms, 27.7MB)
테스트 15 〉	통과 (80.71ms, 27.6MB)
'''
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer