# 명예의 전당(1)
## 0.01ms~3.24ms
def solution(k, score):
    answer, tmp = list(), list()
    for indx, num in enumerate(score):
        tmp.append(num)
        if len(tmp) <= k :
            answer.append(min(tmp))
        else:
            tmp.sort(reverse = True)
            answer.append(tmp[k-1])
    return answer