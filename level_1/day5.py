# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0 :
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)

## 스터디원 한줄 풀이 : lambda함수, filter함수 사용
def solution(arr, divisor):
    answer = sorted(filter(lambda x: x%divisor==0, arr))
    return answer if answer else [-1]

def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    return sorted(answer) if answer else [-1]


# 제일 작은 수 제거하기
##(오답)
## 문제 조건에 배열을 정렬하라는 내용은 없고 min값 제거하라는 내용만 있어서 오답 처리됨.
def solution(arr):
    answer = sorted(arr, reverse=True)[:-1]
    return [-1] if len(arr) == 1 else answer

def solution(arr):
    arr.remove(min(arr)) 
    return [-1] if len(arr)==0 else arr

# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

## 스터디원 한줄 풀이 : lambda함수, map함수 사용
def solution(absolutes, signs):
    return sum(map(lambda x,y: x if y == True else x*(-1), absolutes,signs))

def solution(absolutes, signs):
    return sum(map(lambda x: absolutes[x] if signs[x] else -absolutes[x], range(len(absolutes))))


# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(0, 10):
        answer += i
    return answer - sum(numbers)

## 스터디원 한줄 풀이 : lambda함수, map함수, filter함수 사용
def solution(numbers):
    return sum(filter(lambda x: x not in numbers,range(10)))
    
def solution(numbers):
    return sum(i for i in range(10) if i not in numbers)