# 1차[비밀지도]
def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    # 2진수 변환 
    for b1 in arr1:
        bin_b1 = bin(b1)[2:]
        bin_arr1.append(bin_b1)
        
    for b2 in arr2:
        bin_b2 = bin(b2)[2:]
        bin_arr2.append(bin_b2)
        
    # 공백, # 변환
    for i in range(0, n) :
        s_num = ''
        num = str(int(bin_arr1[i]) + int(bin_arr2[i]))
        if len(num) != n :
            num = str(0)*(n-len(num))+num
        for j in num :
            if j == '0':
                s_num += ' '
            else:
                s_num += '#'
        answer.append(s_num)                
    return answer\

## 스터디원 코드
def solution(n, arr1, arr2):
    arr1 = [bin(x)[2:].zfill(n) for x in arr1]
    arr2 = [bin(x)[2:].zfill(n) for x in arr2]
    return [''.join(' ' if arr1[i][j]=='0' and arr2[i][j] =='0' else '#' for j in range(n)) for i in range(n)]

### string 앞에 0채우는 방법 
# 1. zfill(width)
"2".zfill(3)
## > '002'
"50000".zfill(5)
## > '50000'
"123".zfill(5)
## > '00123'

# 2. rjust(width, [fillchar])
"2".rjust(3, "0")
## > '002'
"50000".rjust(5, "0")
## > '50000'
"123".rjust(5, "0")
## > '00123'
"123".rjust(5, "a")
## > 'aa123'



# 문자열 내 마음대로 정하기
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

## 실패 코드 
def solution(strings, n):
    return sorted(strings, key= lambda x : x[n])

    '''
    테스트 2
    입력값 〉	["abce", "abcd", "cdx"], 2
    기댓값 〉	["abcd", "abce", "cdx"]
    실행 결과 〉	실행한 결괏값 ["abce","abcd","cdx"]이 기댓값 ["abcd","abce","cdx"]과 다릅니다.
    '''
    '''
    제한 조건을 만족하기 위해서 조건을 하나 더 줘야 했음.
    제한 조건 : 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
    '''
