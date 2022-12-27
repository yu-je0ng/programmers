# 가장 가까운 같은 글자
def solution(s):
    answer, alpha_dic = list(), dict()
    for indx, alpha in enumerate(s):
        if alpha not in alpha_dic:
            answer.append(-1)
        else:
            answer.append(indx - alpha_dic[alpha])
        ## 중요 요소.
        alpha_dic[alpha] = indx
    return answer, alpha_dic
'''
문제 조건 : 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알아야 함.
중요 요소인 "alpha_dic[alpha] = indx"을 통해 동일한 alphabet의 최신 인덱스를 저장함.
===========================
최종 결과
입력값 〉	"banana"
기댓값 〉	[-1, -1, -1, 2, 2, 2]
실행 결과 〉 [[-1,-1,-1,2,2,2],{"b":0,"a":5,"n":4}]
'''