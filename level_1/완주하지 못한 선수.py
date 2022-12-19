# try01.
## break를 사용하지 않아서 오류 발생함.
'''
participant와 completion이 다른경우 break가 없기 때문에
해당 시점에서 갑을 반환하지 않고
participant와 completion이 업데이트 됨.
따라서 if문에서 발견이 되었을때 break를 통해 값을 도출해줘야 됨.
'''
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
        else:
            answer = participant[-1]
    return answer

# try02. 통과
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            answer = participant[-1]
    return answer
## ============= 바로 return하는 동일 코드.
def solution(participant, completion):
    participant.sort()
    completion.sort()    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


# try03. 통과 : hash()
## for문보다 빠름.
## hashing : 인덱스 = 데이터를 저장할 위치
def solution(participant, completion):
    hash_dict = dict()
    sum_hash = 0
    for part in participant:
        hash_dict[hash(part)] = part
        sum_hash += hash(part)
    
    for comp in completion:
        sum_hash -= hash(comp)
    
    return hash_dict[sum_hash]

# try04. 통화 : counter()
## 간결하지만, for문 돌리는 것보다 시간 더 걸리는 경우 존재.
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
