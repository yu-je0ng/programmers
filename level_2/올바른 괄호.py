# 올바른 괄호 - 스택(stack)

## try01
def solution(s):
    stack = []
    for i in s:
        if i == '(':  #1 '('는 stack에 추가
            stack.append(i)
        else:  #2 i == ')'인 경우
            if stack == []:  #3 괄호 짝이 ')'로 시작하는 경우 False
                return False
            else:
                stack.pop()  #4 '('가 ')'와 짝일때, stack에서 '('제거
                
    return stack == [] #5 올바른 경우 true

'''
(#2)s가 ')'으로 시작해서 #1을 걸치지 않는 경우, #3에서의 stack은 []값일 것이다.
따라서 처음부터 올바르지 않는 괄호로 판단됨으로 바로 False를 return한다. 

모든 과정을 완료했을때,
'('은 ')'을 만나서 stack에서 pop되었으므로 stack의 결과 값은 []일 것이다.
'''

## try02
def solution(s):
    count = 0
    for i in s:
        count += 1 if i == '(' else -1
        if count < 0:
            return False
    return count == 0
'''
다른 팀원의 정답지의 경우,
자연수를 사용해서 stack의 원리를 이용하여 답을 구했다.
공간 알고리즘측면에서 좋은 효율성을 가질 것 같다고 생각했다.
'''