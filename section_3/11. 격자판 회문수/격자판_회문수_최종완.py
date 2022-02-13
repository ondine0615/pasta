import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

#============================================================================#
N = 7
격자판 = []

def 회문수_검사(배열):
    최대_인덱스 = len(배열) - 1
    for i in range(3):
        if 배열[i] != 배열[최대_인덱스-i]:
            return False

    return True




#============================================================================#

for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#============================================================================#
    격자판 = [list(map(int, input().split())) for _ in range(N)]

    정답 = 0

    for i in range(N):
        for j in range(3):
            if 회문수_검사([격자판[i][j+dx] for dx in range(5)]):
                정답 += 1

            if 회문수_검사([격자판[j+dy][i] for dy in range(5)]):
                정답 += 1

#============================================================================#

    END = time()
    REAL_ANSWER = int(open(pwd + f"\\out{file_no}.txt", 'r').readline().strip())
    if 정답 != REAL_ANSWER:
        print(정답, REAL_ANSWER)
        print("오답")
    else:
        print("정답")

    print(f"실행시간: {END - START}")
