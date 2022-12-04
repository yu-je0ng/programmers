# 3진법 뒤집기
def solution(n):
    answer = ''
    while n > 0:
        # 앞뒤 반전(3진법) : 45  -> 0021
        answer += str(n % 3)
        n = n//3
    return int(answer, 3)

# 예산
def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d :
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer

# 시저 암호
## 1번식 : 아스키코드 사용 (미사용보다 빠른 경우 존재) 
#A~Z => 65~90
#a~z => 97~122 
def solution(s, n):
    answer = []
    for char in s:
        if char == ' ':
            answer += ' '
        elif char < 'a':
            answer += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
    return ''.join(answer)
## 2번식 : 아스키코드 미사용
def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for char in list(s):
        if char == ' ':
            answer += ' '
        elif char == char.lower():
            answer += alpha[(alpha.find(char)+n)%len(alpha)]
        elif char == char.upper():
            answer += alpha[(alpha.find(char.lower())+n)%len(alpha)].upper()
    return answer

# 최소직사각형
def solution(sizes):
    w = []
    h = []
    for size in sizes :
        w += [sorted(size)[0]]
        h += [sorted(size)[1]]
    return sorted(w)[-1] * sorted(h)[-1]
## 리스트 만들지 않고 if문으로 filter : 위의 식보다 빠름.
def solution(sizes):
    w, h = 0, 0
    for size in sizes:
        size.sort()
        if w < size[0]: w = size[0]
        if h < size[1]: h = size[1]
    return w * h
