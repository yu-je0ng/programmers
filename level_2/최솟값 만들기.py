## try01
def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(0, len(A)):
        answer += A[i] * B[i] 
    return answer

## try02
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return sum([A[i]*B[i] for i in range(len(A))])

## try03
def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))