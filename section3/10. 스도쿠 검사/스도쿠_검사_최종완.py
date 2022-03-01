import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

#============================================================================#
N = 9
스도쿠 = []
def 스도쿠_검사():
    #행,열 검사
    for i in range(N):
        행_검사결과 = set()
        열_검사결과 = set()
        for j in range(N):
            행_검사결과.add(스도쿠[i][j])
            열_검사결과.add(스도쿠[j][i])

        if len(행_검사결과) != 9 or len(열_검사결과) != 9:
            return False

    #3x3 검사
    for i in range(3):
        for j in range(3):
            시작_x = 3 * i
            시작_y = 3 * j
            검사_결과 = set()

            for x in range(3):
                for y in range(3):
                    검사_결과.add(스도쿠[시작_x + x][시작_y + y])

            if len(검사_결과) != 9:
                return False

    return True




#============================================================================#

for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#============================================================================#
    스도쿠 = [list(map(int, input().split())) for _ in range(N)]

    정답 = "YES" if 스도쿠_검사() else "NO"

#============================================================================#

    END = time()
    REAL_ANSWER = open(pwd + f"\\out{file_no}.txt", 'r').readline().strip()
    if 정답 != REAL_ANSWER:
        print("오답")
    else:
        print("정답")

    print(f"실행시간: {END - START}")
