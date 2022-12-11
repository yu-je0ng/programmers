# 소수 찾기
## "에라토스테네스의 체" 이용함.
'''
소수(n)의 배수는 약수로 무조건 n을 포함하게 된다.
따라서 절대 소수의 배수는 소수가 될 수 없다는 개념을 이용함.
- 아래의 식에서 set함수를 사용하는 이유는 list 사용시, 연산이 불가능하기 떄문임.(TypeError: unsupported operand type(s) for -=: 'list' and 'list')
    list를 사용하기 위해서는 numpy나 zip함수를 이용해야 됨.
'''
def solution(n):
    num = set(range(2, n+1)) # 2 ~ n까지의 수를 함수 num에 담기
    for i in range(2, int(n**0.5)+1) :  # 2부터 n의 제곱근까지의 수 i에 대해
        if i in num :                   # i가 num에 있으면 
            multi = set(range(2*i, n+1, i)) # 소수의 배수는 소수가 될 수 없으므로
            num -= multi                    # i의 배수 set를 num에서 빼주기.
    return len(num)
'''
# 오답1. for문으로 풀기
## 시간 초과(+효율성 떨어짐)
## 제한 조건 : n은 2이상, 1000000이하의 자연수임.
def solution(n):
    answer = 0
    for i in range(1, n+1) :
        cnt = 0
        for j in range(1, i+1) :
            if i % j == 0:
                cnt +=1
        if cnt == 2 :
            answer += 1
    return answer

def solution(n):
    answer = 0
    for i in range(2, n+1) :
        cnt = 0
        for j in range(2, i) :
            if i % j == 0:
                cnt +=1
        if cnt == 0 :
            answer += 1
    return answer

# 오답2. N의 약수는 N**0.5(sqrt(N))범위에 존재한다
## 시간 초과(+효율성 떨어짐)
## for문 횟수 줄이기.
def solution(n):
    answer = 0
    for i in range(2, n+1) :
        cnt = 0
        for j in range(2, int(i**0.5)+1) :
            if i % j == 0:
                cnt +=1
        if cnt == 0 :
            answer += 1
    return answer
'''
### list -= list
[3, 7] - [1, 2] # TypeError: unsupported operand type(s) for -: 'list' and 'list'
## 1. numpy 이용
import numpy as np
np.array([3, 7]) - np.array([1, 2]) # array([2, 5])

## 2. zip 이용
[a - b for a, b in zip([3, 7], [1, 2])] # [2, 5]



# 모의고사

'''
# 1.오답 
## 수포자의 방식배열 길이가 answer길이보다 긴 경우만 생각함.
### ndarray.tolist() : numpy to list

import numpy as np
def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    num_1 = (np.array(supo1[:len(answers)]) - np.array(answers)).tolist().count(0)
    num_2 = (np.array(supo2[:len(answers)]) - np.array(answers)).tolist().count(0)
    num_3 = (np.array(supo3[:len(answers)]) - np.array(answers)).tolist().count(0)
    
    nums = [num_1, num_3, num_3]
    
    for key, value in enumerate(nums):
        if max(nums) == value :
            answer.append(key+1)
    
    return answer
'''
## answer의 길이와 상관없이 구하기 위해서 나머지(%)를 사용함.
def solution(answers):
    answer = []
    ## 첫번째 for문에서 index를 지정하기 위해서 정확한 range가 지정되어 있어야 함.
    nums = [0, 0, 0]
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for key, val in enumerate(answers):
        if supo1[key%5] == val:
            nums[0] += 1
        if supo2[key%8] == val:
            nums[1] += 1
        if supo3[key%10] == val:
            nums[2] += 1
    
    for key, value in enumerate(nums):
        if max(nums) == value :
            answer.append(key+1)
    
    return answer