# 숫자의 표현

## 모든 부분합을 구하는 방법 : 완전 탐색
### 시간 복잡도 : O(n^2)
def solution(n):
    answer = 0

    for i in range(1, n+1):
        interval_sum = 0
        for j in range(i, n+1):
            interval_sum += j
            if interval_sum == n:
                answer += 1
            elif interval_sum > n :
                break
    return answer 



## 투 포인터 알고리즘을 사용.
### 시간 복잡도 : O(n)
def solution(n):
    m = n
    array = [i for i in range(1, n+1)]

    cnt = 0
    interval_sum = 0
    end = 0

    for start in range(n):
        while interval_sum < m and end < n:
            interval_sum += array[end]
            end += 1
        if interval_sum == m:
            cnt += 1
        interval_sum -= array[start]

    return cnt

