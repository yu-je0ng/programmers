# 2016년
from datetime import datetime
def solution(a, b):
    return datetime(2016, a, b).strftime("%a").upper()
'''
# 수정 과정 1
from datetime import datetime
def solution(a, b):
    return datetime(2016, a, b)

> TypeError: Object of type datetime is not JSON serializable    

# 수정 과정 2
from datetime import datetime
def solution(a, b):
    answer = ''
    print(datetime(2016, a, b))
    print(type(datetime(2016, a, b)))
    print(type(datetime(2016, a, b).strftime("%a")))
    return answer 

> 2016-05-24 00:00:00
> <class 'datetime.datetime'>
> <class 'str'>

" datetime 객체는 json 직렬화가 불가능하기에 
    완성된 답안 처럼 strftime 함수를 사용하여 
    datatime 객체에서 string으로 변환함.
"
'''

# 포켓몬
def solution(nums):
    cnt = len(nums)//2
    cnt_unique = len(set(nums))
    if cnt_unique < cnt:
        cnt = cnt_unique
    return cnt

'''
# 한줄 코드 - min 함수 사용
def solution(nums):
    return min(len(nums)//2, len(set(nums)))
'''
