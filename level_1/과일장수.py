# 과일장수
'''
고민 부분 : 몇 상자를 만들 수 있는가? 
- score의 길이와 담을 수 있는 개수(m)의 몫을 구한다.
'''
## 0.00ms~91.00ms
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True) # 등급 기준 박스 구분 가능.
    box_cnt = len(score) // m # 판매가능한 박스 개수
    for inx in range(1, box_cnt+1):
        low_price = inx * m # 하나의 박스에서의 최저 사과 점수
        price = score[low_price-1] * m # 하나의 박스에서 얻을 수 있는 최대 이익
        answer += price
    return answer