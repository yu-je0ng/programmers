# 신고 결과 받기
'''
[매개변수]
id_list: 이용자의 ID가 담긴 문자열 배열
report: 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열
k: 정지 기준이 되는 신고 횟수

[결과]
return: 각 유저별로 처리 결과 메일을 받은 횟수 
'''
## 0.01ms ~ 4053.14ms
def solution(id_list, report, k):
    answer = {user:0 for user in id_list}
    check_list = {user:0 for user in id_list}
    mail = {user:[] for user in id_list}
    report = list(set(report))

    for r in report:
        mail[r.split()[0]].append(r.split()[1])
        check_list[r.split()[1]] += 1
    
    for c_key, c_val in check_list.items():
        if c_val >= k:
            for m_key, m_val in mail.items():
                if c_key in m_val:
                    answer[m_key] += 1

    return list(answer.values())

## 0.01ms ~ 1223.23ms
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer