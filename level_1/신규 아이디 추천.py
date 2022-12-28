# 신규 아이디 추천
'''
카카오 아이디의 규칙
1. 아이디의 길이는 3자 이상 15자 이하.
2. 아이디의 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)문자만 사용 가능.
3. 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없음. 

카카오 아이디 생성 단계
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
import re
def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계 
    new_id = re.sub(r'[^\w\s\.\-\_]', '', new_id)
    # ------------
    pattern = re.compile(r'[^\w\s\.\-\_]')
    new_id = pattern.sub("", new_id)

    # 3단계
    ## new_id = new_id.replace("..", ".") # 잘못된 방법:2개이상의 마침표(.)는 바꿀 수 없음.
    new_id = re.sub('\.+', '.', new_id)

    # 4단계
    new_id = new_id.strip(".")

    # 5단계
    if not new_id :
        new_id = "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id.rstrip(".")

    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id


