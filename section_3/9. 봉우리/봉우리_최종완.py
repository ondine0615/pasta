import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

#============================================================================#
N = 0
지도_원본 = []
def 봉우리_체크(행, 열):

    상 = 지도_원본[행-1][열] if 행 - 1 >= 0 else 0
    하 = 지도_원본[행+1][열] if 행 + 1 != N else 0
    좌 = 지도_원본[행][열-1] if 열 - 1 >= 0 else 0
    우 = 지도_원본[행][열+1] if 열 + 1 != N else 0
    값 = 지도_원본[행][열]

    if(값 > 상 and 값 > 하 and 값 > 좌 and 값 > 우):
        return True

    return False        

#============================================================================#

for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#============================================================================#
    N = int(input())
    지도_원본 = [list(map(int, input().split())) for _ in range(N)]

    정답 = 0

    for i in range(N):
        for j in range(N):
            if 봉우리_체크(i, j):
                정답 += 1

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
