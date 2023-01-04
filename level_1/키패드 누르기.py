# 키패드 누르기
'''
가운데 키 패드를 누르는 손 구분. -> 좌표 거리 계산.
'''
## try01. 실패
## 원인 : 초기 위치 지정 X
def solution(numbers, hand):
    answer = ''
    pad = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"],["*", "0", "#"]]
    pad_L = ["1", "4", "7"]
    pad_R = ["3", "6", "9"]
    loc_L = ""
    loc_R = ""
    for i in numbers:
        if str(i) in pad_L:
            answer += "L"
            loc_L = str(i)
        elif str(i) in pad_R:
            answer += "R"
            loc_R = str(i)
        else:
            # 좌표 거리 계산
            dis_L = 0
            dis_R = 0
            for m, n, j in zip(loc_L, loc_R, str(i)):
                dis_L = abs(int(m)-int(j))
                dis_R = abs(int(n)-int(j))

            # 왼손이 가까울때
            if dis_L > dis_R:
                answer += "R"
                loc_L = str(i)
            # 오른손이 가까울 떄
            elif dis_L < dis_R:
                answer += "L"
                loc_R = str(i)
            # 두 거리가 같은때
            else:
                if hand == "left":
                    answer += "L"
                    loc_L = str(i)
                else :
                    answer += "R"
                    loc_R = str(i)
    return answer

## try02. 
def solution(numbers, hand):
    answer = ""
    
    # 키패드 좌표
    pad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작 위치
    loc_L = pad['*']
    loc_R = pad['#']
    
    # 왼손 오른손 구분
    pad_L = [1, 4, 7]
    pad_R = [3, 6, 9]

    for num in numbers:
        now = pad[num]
        # 왼손
        if num in pad_L:
            answer += 'L'
            loc_L = now
            
        # 오른손
        elif num in pad_R:
            answer += 'R'
            loc_R = now
            
        # 2, 5, 8, 0을 누르는 경우
        else:
            left_d = 0
            right_d = 0
            
						# 좌표 거리 계산
            for m, n, j in zip(loc_L, loc_R, now):
                left_d += abs(m-j)
                right_d += abs(n-j)
            
            # 왼손이 더 가까운 경우
            if left_d < right_d:
                answer += 'L'
                loc_L = now
                
            # 오른손이 더 가까운 경우
            elif left_d > right_d:
                answer += 'R'
                loc_R = now
            
            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    loc_L = now
                    
                # 오른손잡이 경우
                else:
                    answer += 'R'
                    loc_R = now
    return answer