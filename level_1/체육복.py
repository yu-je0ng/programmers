'''
## 탐욕법 : 그리디 알고리즘(gredy algorithm)
## 현재 상황에서 지금 당장 좋은 것만 고르는 방법(정당성 분석 요함 : 해당 방법에서의 해가 최적의 해가 아닐 수 있음.)

전체 학생의 수 n
체육복을 도난당한 학생들의 번호가 담긴 배열 lost
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
'''

# try01. 실패
## 제한 사항 충족하지 못함.
'''
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''
def solution(n, lost, reserve):
    answer = n - len(lost)
    for student in reserve:
        front, back = student + 1, student - 1 
        if front in lost or back in lost :
            answer += 1
            reserve.remove(student)
    return answer 

# try02. 실패
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    # lost = reserve 인 학생 제거.
    for student in reserve : 
        if student in lost :
            reserve.remove(student)
            lost.remove(student)

    # 여분의 체육복 빌려주기.
    for student in reserve:
        front, back = student - 1, student + 1 
        if front in lost:
            answer += 1
            reserve.remove(student)
        elif back in lost:
            answer += 1
            reserve.remove(student)
    return answer
'''
==================
테스트 3
입력값 〉	5, [4, 2], [3, 5]
기댓값 〉	5
실행 결과 〉	실행한 결괏값 4이 기댓값 5과 다릅니다.
==================
테스트 4
입력값 〉	5, [5], [1]
기댓값 〉	4
실행 결과 〉	테스트를 통과하였습니다.
'''

# try03. 실패
## set 차집합 이용.
## 80.0 / 100.0 : test17~20, test25 실패
'''
원인 : 체육복을 빌려줄때 뒷번호 학생부터 빌려줌.
만약, 체육복을 빌려줄 수 있는 학생이 3번 5번 이고 체육복이 없는 학생이 2번 4번일때
3번학생은 4번학생을 먼저 빌려줘버림.
2번 학생은 3번 학생에게 체육복을 빌리고 4번 학생이 5번 학생에게 체육복을 빌리는 이상적인 방법이 있으나
이를 반영하지 못한 알고리즘 식임.
'''
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for student in set_lost:
        if student + 1 in set_reserve:
            set_reserve.remove(student + 1)
        elif student - 1 in set_reserve:
            set_reserve.remove(student - 1)
        else:
            n-=1
    return n

# try04. 통과
## set 차집합 이용.
## try03번에서 빌려주는 순서를 바꿈.(else를 return에 반영함.)
def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for student in set_reserve:
        if student - 1 in set_lost:
            set_lost.remove(student - 1)
        elif student + 1 in set_lost:
            set_lost.remove(student + 1)
    return n-len(set_lost)

# =======================================
# try02와 try03의 차이1 : list와 set의 차이.
## try02. 
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    # lost = reserve 인 학생 제거.
    for student in reserve : 
        if student in lost :
            reserve.remove(student)
            lost.remove(student)
            
    answer = n - len(lost)
    
    print(f'lost:{lost}') # lost:<class 'list'>
    print(f'reserve:{reserve}') # reserve:<class 'list'>
    return answer
'''
테스트 1
입력값 〉	5, [2, 4], [1, 3, 5]
기댓값 〉	5
실행 결과 〉	실행한 결괏값 3이 기댓값 5과 다릅니다.
출력 〉	lost:[2, 4]
    reserve:[1, 3, 5]
==================
테스트 2
입력값 〉	5, [2, 4], [3]
기댓값 〉	4
실행 결과 〉	실행한 결괏값 3이 기댓값 4과 다릅니다.
출력 〉	lost:[2, 4]
    reserve:[3]
==================
테스트 3
입력값 〉	5, [4, 2], [3, 5]
기댓값 〉	5
실행 결과 〉	실행한 결괏값 3이 기댓값 5과 다릅니다.
출력 〉	lost:[2, 4]
    reserve:[3, 5]
'''
## try03. 
def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    print(f'new_lost:{new_lost}') # new_lost:<class 'set'>
    print(f'new_reserve:{new_reserve}') # new_reserve:<class 'set'>
    return n
'''
테스트 1
입력값 〉	5, [2, 4], [1, 3, 5]
기댓값 〉	5
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	new_lost:{2, 4}
    new_reserve:{1, 3, 5}
========================
테스트 2
입력값 〉	5, [2, 4], [3]
기댓값 〉	4
실행 결과 〉	실행한 결괏값 5이 기댓값 4과 다릅니다.
출력 〉	new_lost:{2, 4}
    new_reserve:{3}
========================
테스트 3
입력값 〉	5, [4, 2], [3, 5]
기댓값 〉	5
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	new_lost:{2, 4}
    new_reserve:{3, 5}
'''
# =======================================
