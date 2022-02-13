import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

def 낭비길이_구하기(DVD길이, 곡길이들):
    낭비_길이 = 0
    누적_길이 = 0
    배열길이 = len(곡길이들)
    for i in range(0, 배열길이):
        누적_길이 += 곡길이들[i]
        
        if 누적_길이 == DVD길이:
            누적_길이 = 0
        elif 누적_길이 > DVD길이:
            낭비_길이 += (DVD길이 - 누적_길이 - 곡길이들[i])
            i -= 1
            누적_길이 = 0
    return 낭비_길이

def DVD_갯수_구하기(DVD길이, 곡길이들):
    갯수 = 0
    누적_길이 = 0
    카운트시작 = False
    배열길이 = len(곡길이들)
    for i in range(0, 배열길이):
        누적_길이 += 곡길이들[i]
        
        if 누적_길이 < DVD길이:
            카운트시작 = True
        elif 누적_길이 > DVD길이:
            갯수 += 1
            누적_길이 = 곡길이들[i]
            카운트시작 = True
        else:
            갯수 += 1
            누적_길이 = 0
            카운트시작 = False

    if 카운트시작:
        갯수 += 1

    return 갯수

for i in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{i}.txt", 'r')

#============================================================================#
    # 주어진 것
    # N 곡의 갯수, M DVD 갯수
    # 곡의 길이

    # 구하고자 하는 것
    # 최적의 DVD길이

    # 자르는 길이와 만들어진 DVD 갯수의 연관관계
    # 길이가 길어질수록 갯수는 적어진다

    정답 = -1
    N, DVD_갯수 = map(int, input().split())
    곡길이들 = list(map(int, input().split()))

    시작, 끝 = 1, sum(곡길이들)
    만들어진갯수 = -1

    while 시작 <= 끝:

        중간 = (시작 + 끝) // 2
        만들어진갯수 = DVD_갯수_구하기(중간, 곡길이들)

        if 만들어진갯수 > DVD_갯수:
            시작 = 중간 + 1
        else:
            
            끝 = 중간 - 1

    정답 = 시작


#============================================================================#

    END = time()
    if 정답 == int(open(pwd + f"\\out{i}.txt", 'r').readline()):
        print("정답")
    else:
        print("오답")
    print(f"실행시간: {END - START}")
