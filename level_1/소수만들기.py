# 소수 만들기
from itertools import combinations
def solution(nums):
    answer = 0
    combs = list(combinations(nums,3))
    
    for comb in combs:
        check = 0
        comb_sum = sum(comb)
        # 소수 판별
        for i in range(2, int(comb_sum**0.5)+1):
            if comb_sum % i == 0:
                check += 1
        if check == 0:
            answer += 1
    return answer

