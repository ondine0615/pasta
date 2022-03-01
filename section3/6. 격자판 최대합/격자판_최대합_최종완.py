import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치


for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#====================================================================4========#

    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    정답 = 0
    sumOfGrid = []


    #가로, 세로로 더하기
    for i in range(N):
        verticalTotal = 0
        horizentalTotal = 0
        for j in range(N):
            horizentalTotal += grid[i][j]
            verticalTotal += grid[j][i]

        sumOfGrid.append(verticalTotal)
        sumOfGrid.append(horizentalTotal)

    #대각
    total = 0
    for i in range(N):
        total += grid[i][i]
    sumOfGrid.append(total)

    total = 0
    for i in reversed(range(0, N)):
        total += grid[i][i]
    sumOfGrid.append(total)

    정답 = max(sumOfGrid)

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
