# 문자열 나누기
## try01. 실패
'''
dict형을 사용해서 동일한 값을 찾으려고 했으나, 이중 for문을 만들어야 할 것 같아 다른 방법 강구함.

또한 조건에서 "x와 x가 아닌 다른 글자들이 나온 횟수를 각각 세고, 두 횟수가 같아지는 순간"이라고 명시한 것을 파악.
모든 문자열에 대한 횟수를 각각 카운트해야된다고 잘못 생각했다는 것을 깨닭음.
'''
def solution(s):
    answer = 0
    dict_s = {i :0 for i in set(s)}
    for j in s:
        dict_s[j] += 1
        if dict_s.values() :
            print(dict_s.values())
    return answer

## try02. 성공
## 0.00ms ~ 0.96ms
def solution(s):
    answer = 0
    char = ""
    cnt_orig = 0
    cnt_comp = 0
    for i in s:
        if char == "":
            char = i
            cnt_orig += 1
        else :
            if char == i:
                cnt_orig += 1
            else :
                cnt_comp += 1
            # x와 x가 아닌 다른 글자들이 나온 횟수가 동일해질때.
            if cnt_orig == cnt_comp:
                answer += 1
                # 초기화 : 문자열 분리
                char = ""
                cnt_orig = 0
                cnt_comp = 0
    # 마지막 글자 남았을때 - test2
    if char != "":
        answer += 1
    return answer

## try03. 변수 리스트화
## 0.00ms ~ 1.66ms : 보다 시간이 더 걸림.
def solution(s):
    answer = 0
    list_s = ["", 0, 0]
    for i in s:
        if list_s[0] == "":
            list_s[0] = i
            list_s[1] += 1
        else :
            if list_s[0] == i:
                list_s[1] += 1
            else:
                list_s[2] += 1
            if list_s[1] == list_s[2]:
                answer += 1
                list_s = ["", 0, 0]
    if list_s[0] != "":
        answer += 1
    return answer