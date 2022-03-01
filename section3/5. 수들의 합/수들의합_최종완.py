import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치


for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#====================================================================4========#

    N, M = map(int, input().split())
    배열 = list(map(int, input().split()))
    정답 = 0

    for i in range(0, N):
        총합 = 0
        j = i
        while 총합 < M and j < N:
            총합 += 배열[j]
            j += 1

        if 총합 == M:
            정답 += 1

        # for j in range(i, N):
        #     총합 += 배열[j]
        #     if 총합 == M:
        #         정답 += 1
        #         break
        #     if 총합 > M:
        #         break

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
