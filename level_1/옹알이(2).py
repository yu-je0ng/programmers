# 옹알이
'''
할 수 있는 발음 : "aya", "ye", "woo", "ma"
- 위의 네가지 발음 조합된 단어 가능
- 하나의 발음을 연속으로 할 수 없음.
'''
## try01. 실패
## 정확성 50.0/100.0
def solution(babbling):
    answer = 0
    prons = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for pron in prons:
            if pron*2 not in bab: # 같은 발음 연속 못함.
                bab = bab.replace(pron, "")
        if not bab:
            answer += 1
    return answer

# ===========================================
def solution(babbling):
    answer = 0
    prons = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        print("="* 10)
        for pron in prons:
            if pron*2 not in bab: # 같은 발음 연속 못함.
                bab = bab.replace(pron, " ")
        print(f"|{bab}|")
    return answer
'''
# 테스트 1
입력값 〉	["aya", "yee", "u"]
기댓값 〉	1
실행 결과 〉	실행한 결괏값 0이 기댓값 1과 다릅니다.
출력 〉	
==========
| |
==========
| e|
==========
|u|

# 테스트 2
입력값 〉	["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
기댓값 〉	2
실행 결과 〉	실행한 결괏값 0이 기댓값 2과 다릅니다.
출력 〉	
==========
|  |
==========
|uuu|
==========
|yeye|
==========
|   |
==========
|ayaayaa|
'''
# =========================================

# try02.
## 0.01ms ~ 0.15ms
def solution(babbling):
    answer = 0
    prons = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for pron in prons:
            if pron*2 not in bab: # 같은 발음 연속 못함.
                bab = bab.replace(pron, " ")
        if not bab.strip(): 
            answer += 1
    return answer
'''
for문 안에 if not으로 filter걸어줘서 발음할 수 있는 단어 개수 count
'''