# k번째 수
def solution(array, commands):
    ## 런타임 에러
    # answer = [sorted(array[commands[0][0]-1 : commands[0][1]])[commands[0][2]-1],sorted(array[commands[1][0]-1 : commands[1][1]])[commands[1][2]-1],sorted(array[commands[2][0]-1 : commands[2][1]])[commands[2][2]-1]]
    return [sorted(array[c[0]-1:c[1]])[c[2]-1] for c in commands]

# 숫자 문자열과 영단어
def solution(s):
    dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for key, value in dic.items():
        if key in s:
            s = s.replace(key, str(value))
    return int(s)

