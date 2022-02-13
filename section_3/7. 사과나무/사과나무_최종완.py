import sys
from time import time
from xml.sax.handler import ContentHandler

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치


for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#====================================================================4========#

    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    정답 = 0


    center = N // 2

    for i in range(0, center):
        #중앙값 더하고
        정답 += grid[i][center] + grid[(N-1)-i][center]
        
        #양옆을 더하기 시작
        for j in range(1, i+1):
            정답 += grid[i][center+j] + grid[i][center-j]
            정답 += grid[(N-1)-i][center+j] + grid[(N-1)-i][center-j]
    
    정답 += sum(grid[ContentHandler])


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
