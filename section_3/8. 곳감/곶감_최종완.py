from cgi import test
import sys
from time import time
from xml.sax.handler import ContentHandler

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

#============================================================================#
def 배열_회전(배열, 방향, 회전횟수):
    결과 = 배열[:]

    if 방향: #True시 왼쪽
        for _ in range(회전횟수):
            결과 = [결과[-1]] + 결과[:-1]

    else: # False시 오른쪽
        for _ in range(회전횟수):
            결과 = 결과[1:] + [결과[0]]

    return 결과
#============================================================================#

for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#============================================================================#

    # N x N의 격자 (N은 홀수)
    N = int(input())
    격자 = [list(map(int, input().split())) for _ in range(N)]
    # x번째 행을 0, 1에 따라(왼쪽, 오른쪽) y만큼 회전
    M = int(input())
    명령 = [map(int, input().split()) for _ in range(M)] 
    정답 = 0


    #배열 회전
    for 행, 방향, 회전횟수 in 명령:
        행_인덱스 = 행 - 1
        격자[행_인덱스] = 배열_회전(격자[행_인덱스], 방향, 회전횟수) 

    #합 구하기
    중앙 = N // 2
    배열_길이 = N-1
    
    for 차수 in range(0, 중앙):

        for 인덱스 in range(차수, N-차수):
            정답 += 격자[배열_길이-차수][인덱스] + 격자[차수][인덱스]

    정답 += 격자[중앙][중앙]




#============================================================================#

    END = time()
    REAL_ANSWER = int(open(pwd + f"\\out{file_no}.txt", 'r').readline().strip())
    if 정답 != REAL_ANSWER:
        print(정답)
        print(REAL_ANSWER)
        print("오답")
    else:
        print("정답")

    print(f"실행시간: {END - START}")
