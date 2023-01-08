# 최댓값과 최솟값
## try01. 실패
## list안의 요소가 str임.(음수고려 X)
def solution(s):
    answer = ''
    s = s.split(" ")
    return f"{min(s)} {max(s)}"

## try02. 성공.
## 0.02ms ~ 0.06ms
def solution(s):
    s_list = sorted([int(i) for i in s.split()])
    return str(s_list[0]) + ' ' + str(s_list[-1])

## try03. 성공 풀이.
## 0.03ms ~ 0.03ms
## map 함수 사용시 list요소 int로 지정 가능함.
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))