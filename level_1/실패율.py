# 실패율
'''
전체 스테이지의 개수 N
게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
- 입출력 예
N	stages	                    result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	                [4,1,2,3]
'''
# try01.
## 런타임 에러 : 70.4 / 100.0
## 스테이지를 끝까지 완료하지 못하는 경우를 고려하지 못함. 
'''
100 스테이지가 있을 경우, 
모든 유저가 50까지만 도달하지 못했을때 
나머지 스테이지(51~100)에 대한 실패율을 구하는 조건문이 없음.
'''
def solution(N, stages):
    failure_rate = {} # 각 단계마다의 실패율 
    players = len(stages) # 게임참여자의 수

    for stage in range(1, N+1):
        player_count = stages.count(stage)
        failure_rate[stage] = player_count/players
        # e.g. {1: 1/8, 2:3/7, ...}
        players -= player_count # 다음 단계에 도달하지 못한 플레이어 제거.
        
    answer = sorted(failure_rate.keys(), key=lambda key: failure_rate[key], reverse=True)
    return answer

# try02.
## 0.01ms ~ 1376.02ms
def solution(N, stages):
    failure_rate = {} # 각 단계마다의 실패율 
    players = len(stages) # 게임참여자의 수

    for stage in range(1, N+1):
        if players != 0:
            player_count = stages.count(stage)
            failure_rate[stage] = player_count/players
            # e.g. {1: 1/8, 2:3/7, ...}
            players -= player_count # 다음 단계에 도달하지 못한 플레이어 제거.
        else: # 아무도 특정 스테이지에 도달하지 못했을때.
            failure_rate[stage] = 0 
    
    # sorted(failure_rate.keys()) == sorted(failure_rate)
    ## failure_rate는 dictionary임으로 sorted에 failure_rate를 그냥 넘기면 failure_rate의 key가 들어감.
    # reverse=True 
    ## 내림차순 기준 정렬.
    ## python 3.7부터 dictionary는 순서를 보장함. 
    ## 같은 실패율을 가진 key(stage)라도 순서를 보장해서 정렬됨.
    answer = sorted(failure_rate, key=lambda key: failure_rate[key], reverse=True)

    return answer

# try03.
## 0.03ms ~ 18.59ms
def solution(N, stages):
    answer = []
    failure_rate = []
    info = [0] * (N + 2) # stage : 0단계 ~ N+1단계까지.
    
    # 해당 stage 통과하지 못한 사람 count
    for stage in stages:
        info[stage] += 1
        
    for stage in range(N):
        be = sum(info[(stage + 1):])
        yet = info[stage + 1]
        # 해당 stage를 통과한 사람이 없을 때.
        if be == 0:
            failure_rate.append((str(stage + 1), 0))
        # 실패율 계산
        else:
            failure_rate.append((str(stage + 1), yet / be))
            
    # 테스트 1 : print(failure_rate)
    # [('1', 0.125), ('2', 0.42857142857142855), ('3', 0.5), ('4', 0.5), ('5', 0.0)]

    for item in sorted(failure_rate, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))

    return answer