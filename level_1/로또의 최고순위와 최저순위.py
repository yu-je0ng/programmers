# try01. 
# 0바꾸기에서 결과 도출하지 못함.
def solution(lottos, win_nums):
    answer = []
    lotto_nums = []
    cnt = 0
    # 기존에서 일치하는 번호 count
    for value in lottos:
        if value in win_nums :
            cnt += 1
            win_nums.pop(win_nums.index(value))
    
    # 0 바꾸기.
    for value in lottos:
        if value == 0 :
            lottos[value.index()] = win_nums
                  
        
    return lottos, win_nums, cnt

# ----------------------------------------------

# try02. 
# test12 error 
def solution(lottos, win_nums):
    answer = []
    zero = 0
    cnt = 0
    
    # 기존 일치하는 값과 0의 갯수 count
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1    
        if lotto == 0:
            zero += 1
 
    if zero == 0 & cnt == 0 :
        answer.append(6)
    else:
        answer.append(7 - (cnt+zero))
        
    if cnt == 0: 
        answer.append(6)
    else:
        answer.append(7 - cnt)

    return answer

# ----------------------------------------------

# try03. 통과
# 논리연산자(and)와 비교연산자(&) 구분해서 사용해야 됨.
def solution(lottos, win_nums):
    answer = []
    zero = 0
    cnt = 0
    
    # 기존 일치하는 값과 0의 갯수 count
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1    
        if lotto == 0:
            zero += 1

    # not zero and not cnt   
    if zero == 0 and cnt == 0 :
        answer.append(6)
    else:
        answer.append(7 - (cnt+zero))
        
    if cnt == 0: 
        answer.append(6)
    else:
        answer.append(7 - cnt)

    return answer

'''
&와 |는 비트 연산자이고, &&와 ||는 논리 연산자임.
- 비트 연산자(&, |)
    - &는 특정 변수를 각 비트별로 AND 연산을 하여 그 값을 도출해 내는 것.
    - 비트단위로 사칙연산과 같은 값의 계산을 위해 사용되는 것.
- 논리 연산자(&&, AND, ||, OR)
    - &&는 변수의 값 자체의 논리 값을 AND 연산해 결과 값 또한 논리 값으로 표현.
    - True /False를 구분하기 위해 사용됨.
출처 : https://r2adve.tistory.com/239
'''