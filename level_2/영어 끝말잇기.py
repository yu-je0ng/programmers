# 영어 끝말잇기
def solution(n, words):
    answer = [0,0]
    stack = [words[0]] # 첫번째 단어 고정
    
    for i in range(1, len(words)):
        # "중복없는 단어" & "앞사람이 말한 단어의 마지막 문자로 시작하는 단어"
        if words[i] not in stack and stack[-1][-1] == words[i][0]:
            stack.append(words[i])
        else:
            answer[0] = (i % n) + 1 # 가장 먼저 탈락하는 사람의 번호
            answer[1] = i // n + 1  # 그 사람이 자신의 몇 번째 차례에 탈락하는지
            break
            
    return answer