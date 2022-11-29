# 가운데 글자 가져오기
def solution(s):
    answer = ''
    center = int(len(s)/2)
    if len(s) % 2 == 0 :
        answer = s[center-1:center+1]
    else :
        answer = s[center:center+1]
    return answer
## 스터디원 한 줄 풀이
def solution(s):
    return (lambda x: s[x] if len(s)%2 == 1 else s[x-1:x+1])(len(s)//2)

# 수박수박수박수박수박수?
def solution(n):
    answer = '수박' * n
    return answer[:n]

# 내적
def solution(a, b):
    answer = 0
    for i in range(0, len(a)) :
        c = a[i] * b[i]
        answer += c
    return answer
## 스터디원 한 줄 풀이
def solution(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))
def solution(a, b):
		return sum(x*y for x, y in zip(a, b))
        

# 문자열 내림차순으로 배치하기
def solution(s):
    return ''.join(sorted(s, reverse=True))

'''
sorted(s, reverse=True)
> ["g","f","e","d","c","b","Z"]
## 공백을 기점으로 join
''.join(sorted(s, reverse=True))
> gfedcbZ
'''


