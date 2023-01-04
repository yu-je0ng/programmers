# 크기가 작은 부분 문자열
def solution(t, p):
    answer = 0
    sli_len = len(p)
    for idx, val in enumerate(t):
        char = t[idx:idx+sli_len]
        if len(char) == sli_len and char <= p :
            answer += 1
    return answer