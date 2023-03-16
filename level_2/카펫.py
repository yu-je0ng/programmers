# 카펫 | 완전탐색
'''
1. 가로(width) > 세로(length)
2. brown + yellow = w * l = area(총 면적)
3. yellow = (w-2)*(l-2) # 갈색으로 감싸지기 때문에 
'''
def solution(brown, yellow):
    answer = []
    area = brown + yellow
    for l in range(3, area+1): # 세로는 최소 3부터 시작(1<=yellow<=2000000)
        if area % l == 0 : 
            w = area/l
            if (w-2) * (l-2) == yellow:
                answer = [w,l]
                break
    return answer