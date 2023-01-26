# 크레인 인형뽑기 게임
'''
board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하
board의 각 칸에는 0 이상 100 이하인 정수
    0은 빈 칸
    1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냄

moves 배열의 크기는 1 이상 1,000 이하
moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수
'''
## 통과 (1.47ms, 10.2MB)
def solution(board, moves):
    stacklist = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0
                # 동일한 인형일때
                if len(stacklist) > 1 and stacklist[-1] == stacklist[-2]:
                    stacklist.pop()
                    stacklist.pop()
                    answer += 2     
                break
    return answer

# ===============
...
for i in moves:
    for j in range(len(board)):
        if board[j][i-1] != 0:
            print(j)
            print(i-1)
            print(board[j][i-1])
            print("*"*10)
            stacklist.append(board[j][i-1])
            board[j][i-1] = 0
...
'''
0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1
==============
print(j)
> 3
print(i-1)
> 0
print(board[j][i-1])
> 4
'''
