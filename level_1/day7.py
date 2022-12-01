# 문자열 다루기 기본
def solution(s):
    return True if s.isdigit() and (len(s) == 4 or len(s) == 6) else False
## 스터디원 풀이 : return 값이 True가 나오는 boolean식이면 굳이 else 사용하지 않아도 됨.
def solution(s):
    return s.isnumeric() and (len(s) == 4 or len(s) == 6)

# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0 :
                cnt += 1
        if cnt % 2 == 0 :
            answer += i
        else : 
            answer -= i
    return answer
## 약수 구하는 쉬운 방법
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


# 부족한 금액 계산하기
def solution(price, money, count):
    pay = 0
    for i in range(1, count +1):
        pay += price * i
    return pay - money if pay > money else 0
## 등차 수열 이용한 풀이
### 3,6,9,...을 수열이라 보고 등차수열의 합 공식을 구해주면 price*(count**2)+count//2 - money 식이 도출됨.
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)


# 행렬의 덧셈
## 풀이1
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp=[]
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)
    return answer

## 풀이2
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

## numpy 
import numpy as np
def solution(arr1, arr2):
    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)
    sum_arr = np_arr1 + np_arr2
    
    return sum_arr.tolist()

## zip()
def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        temp = []
        for c, d in zip(a, b):
            temp.append(c+d)
        answer.append(temp)
    return answer

## zip list comprehension
def solution(arr1, arr2):
		answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
		return answer

## 스터디원 한줄 풀이
def solution(arr1, arr2):
    return [[arr1[r][c] + arr2[r][c] for c in range(len(arr1[0]))] for r in range(len(arr1))]