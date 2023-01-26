# 개인정보 수집 유효기간
'''
약관마다 개인정보 보관 유효기간이 정해져 있음.
모든 달은 28일까지 있다고 가정

매개변수
오늘 날짜를 의미하는 문자열 today, 
약관의 유효기간을 담은 1차원 문자열 배열 terms와 
    "약관 종류 유효기간" 형태의 약관 종류와 유효기간을 공백 하나로 구분한 문자열
수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies
    "날짜 약관 종류" 형태의 날짜와 약관 종류를 공백 하나로 구분한 문자열
'''
## try01
'''
단순히 월의 숫자만 빼서 산술연산
'''
def solution(today, terms, privacies):
    answer = []
    t_dict = {}
    
    for i in terms:
        t_dict[i.split()[0]] = i.split()[1]
        
    for j in privacies:
        month = int(t_dict[j.split()[1]]) + int(today[5:7])
        print(today[:5] + str(month) + today[7:])
        
    return answer
'''
-> 문제발생 : 12월이 넘어가서 연단위가 바뀌는 경우와, 문자열의 길이가 안 맞는 경우 발생함.
2022.11.19
2022.17.19
2022.8.19
2022.8.19
'''

## try02
from datetime import datetime, timedelta

def solution(today, terms, privacies):
    date = datetime.strptime(today,'%Y.%m.%d')
    answer = []
    t_dict = {}
    
    for i in terms:
        t_dict[i.split()[0]] = i.split()[1]
        
    for j in privacies:
        week_cnt = int(t_dict[j.split()[1]]) * 4
        validata = date+timedelta(weeks=week_cnt)
        print(validata)
    return answer
'''
문제 발생 : 기존의 모듈을 사용하면, "모든 달은 28일까지 있다"고 가정하는 것과 괴리 발생함.

'''

## try03
def solution(today, terms, privacies):
    answer = []
    
    # today -> 하루단위로 바꾸기(단위통일)
    t_year, t_month, t_day = today.split('.')
    today = int(t_year)*12*28 + int(t_month)*28 + int(t_day)

    # 약관 딕셔너리 {약관 종류:유효기간(일 단위)}
    terms = {i[:1] : int(i[2:]) *28 for i in terms}


    for idx, val in enumerate(privacies):
        v_year, v_month, v_day = val.split('.')
        v_day, v_val = v_day.split() # "."을 기준으로 분류하였기에 마지막에 약관종류와 일을 나눠줌.
        check = int(v_year)*12*28 + int(v_month)*28 + int(v_day)


        # (수집일자 + 약관종류에 따른 일자)가 today을 넘지 않으면 정답(인덱스+1)에 추가
        if check + terms[v_val] <= today:
            answer.append(idx+1)

    return answer