# 성격유형검사
## try01. 성공
## 0.01ms ~ 0.38ms
def solution(survey, choices):
    char = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    answer = ''
    for inx, val in enumerate(survey):
        if choices[inx] < 4 : 
            char[val[0]] += abs(choices[inx] - 4)
        else : 
            char[val[1]] += abs(choices[inx] - 4)
            
    answer += "R" if char["R"] >= char["T"] else "T"
    answer += "C" if char["C"] >= char["F"] else "F"
    answer += "J" if char["J"] >= char["M"] else "M"
    answer += "A" if char["A"] >= char["N"] else "N"
    
    return answer


## try02. 람다함수 활용.
## 0.01ms ~ 0.38ms
def solution(survey, choices):
    char = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    answer = ''
    for inx, val in enumerate(survey):
        if choices[inx] < 4 : 
            char[val[0]] += abs(choices[inx] - 4)
        else : 
            char[val[1]] += abs(choices[inx] - 4)

    return "".join(list(map(lambda x,y: x if char[x] >= char[y] else y, ["R","C","J","A"],["T","F","M","N"])))