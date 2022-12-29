# 기사단원의 무기
## try01. 실패
'''
1 ≤ number ≤ 100,000
num_dic만드는 부분에서 시간초과 발생함.
'''
def solution(number, limit, power):
    num_dic = {str(n):0 for n in range(1, number+1)}
    for cnt in range(1, number+1):
        cnt_check = cnt
        while cnt_check != 0:
            # 각 숫자의 소수 count
            if cnt%cnt_check == 0: num_dic[str(cnt)] += 1
            # limit를 넘은 공격자 filter
            if num_dic[str(cnt)] > limit : 
                num_dic[str(cnt)] = limit-1
                break 
            cnt_check -= 1
    return sum(num_dic.values())

## try02. 성공
## 0.00ms ~ 1133.17ms
def yak_su(num):
    count = 0
    # 약수 구하기 - 에라토스테네스의 체
    for n in range(1, int(num**0.5)+1):
        if num % n == 0:
            if num // n == n : # e.g) 9의 약수 중, 3의 경우
                count += 1
            else : 
                count += 2
    return count

def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        arm = yak_su(num)
        if arm > limit :
            answer += power
        else:
            answer += arm
    return answer