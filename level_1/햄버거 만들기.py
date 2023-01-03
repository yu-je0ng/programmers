# 햄버거 만들기
'''
햄버거 조건 : [빵, 야채, 고기, 빵] = [1, 2, 3, 1] 
1. stack 자료 구조 - 후입 선출
2. 인덱싱(뒤에서부터)
'''
# 0.00ms ~ 175.06ms
def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1, 2, 3, 1]: # stack : 후입선출(LIFO, Last-In-First-Out)
            answer += 1
            for _ in range(1, 5):
                burger.pop()
    return answer