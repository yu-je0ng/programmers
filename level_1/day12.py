# 삼총사
from itertools import combinations
def solution(number):
    answer = 0
    for i in list(combinations(number, 3)) :
        if sum(i) == 0 :
            answer += 1
    return answer

### 한줄 풀이
from itertools import combinations
def solution(number):
    return sum(1 for num in combinations(number, 3) if sum(num) == 0)

'''
combination 
## 하나의 리스트에서 모든 조합을 계산해야 할때, permutations 또는 combinations을 사용.
## 두 개 이상의 리스트에서 모든 조합을 계산해야 할때, product를 사용.
''' 
items = ['1', '2', '3', '4', '5']

from itertools import permutations
list(permutations(items, 2))
# > [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '1'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '5'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4')]

from itertools import combinations
list(combinations(items, 2))
# > [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

from itertools import product
items = [['a', 'b', 'c,'], ['1', '2', '3', '4'], ['!', '@', '#']]
list(product(*items))
# > [('a', '1', '!'), ('a', '1', '@'), ('a', '1', '#'), ('a', '2', '!'), ('a', '2', '@'), ('a', '2', '#'), ('a', '3', '!'), ('a', '3', '@'), ('a', '3', '#'), ('a', '4', '!'), ('a', '4', '@'), ('a', '4', '#'), ('b', '1', '!'), ('b', '1', '@'), ('b', '1', '#'), ('b', '2', '!'), ('b', '2', '@'), ('b', '2', '#'), ('b', '3', '!'), ('b', '3', '@'), ('b', '3', '#'), ('b', '4', '!'), ('b', '4', '@'), ('b', '4', '#'), ('c,', '1', '!'), ('c,', '1', '@'), ('c,', '1', '#'), ('c,', '2', '!'), ('c,', '2', '@'), ('c,', '2', '#'), ('c,', '3', '!'), ('c,', '3', '@'), ('c,', '3', '#'), ('c,', '4', '!'), ('c,', '4', '@'), ('c,', '4', '#')]

# ------------------------------------------

# 두 개 뽑아서 더하기
## 오답 - 4, 5번
from itertools import combinations
def solution(numbers):
    return list(set(sum(num) for num in combinations(numbers, 2)))

## 오답식에서 정렬해야 됨.
from itertools import combinations
def solution(numbers):
    return sorted(list(set(sum(num) for num in combinations(numbers, 2))))

### 스터디원 - combination 미사용
def solution(numbers):
    sets = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sets.add(numbers[i] + numbers[j])
    return sorted(list(sets))
    
def solution(nums):
    return sorted(list(set([nums[i]+nums[j] for i in range(len(nums)) for j in range(i+1, len(nums))])))