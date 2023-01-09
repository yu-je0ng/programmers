# JadenCase 문자열 만들기.

## try01. 실패
def solution(s):
    answer = s.title()
    return answer
'''
테스트 1
입력값 〉	"3people unFollowed me"
기댓값 〉	"3people Unfollowed Me"
실행 결과 〉	실행한 결괏값 "3People Unfollowed Me"이 기댓값 "3people Unfollowed Me"과 다릅니다.
# title() 함수는 조건*을 만족하지 못함.
# 조건* : 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다.
'''

## try02. 성공
## 0.00ms ~ 0.01ms
'''
조건** :s는 길이 1 이상 200 이하인 문자열 
'''
def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return ' '.join(s)


## try03. 성공
## 0.00ms ~ 0.01ms
'''
title 함수와 달리, 맨 앞에 나온 숫자도 문자 취급하여 성공함.
'''
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])