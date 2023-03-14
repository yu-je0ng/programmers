# 짝지어 제거하기.
'''
stack을 활용한 풀이.
'''
def solution(s):
    answer = 0
    stack = []
    
    for i in s:
        if len(stack) == 0 : # s[0]
            stack.append(i)
        else:
            if stack[-1] == i :
                stack.pop()
            else:
                stack.append(i)
                
    if len(stack) == 0: # 문자열 모두 제거되는 s일때
        answer = 1
        
    return answer