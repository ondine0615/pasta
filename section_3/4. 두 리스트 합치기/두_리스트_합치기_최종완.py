import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치


for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#============================================================================#

    배열 = []
    정답 = ""

    입력 = [input().split() for _ in range(0,4)]

    배열1 = list(map(int, 입력[1]))
    배열2 = list(map(int, 입력[3]))
    
    for x in 배열1:
        배열.append(x)

    for x in 배열2:
        배열.append(x)

    배열.sort()

    for x in 배열:
        정답 += str(x) + " "

    정답 = 정답.rstrip()


#============================================================================#

    END = time()
    REAL_ANSWER = open(pwd + f"\\out{file_no}.txt", 'r').readline()
    if 정답 != REAL_ANSWER:
        print(정답)
        print(REAL_ANSWER)
        print("오답")
    else:
        print("정답")

    print(f"실행시간: {END - START}")
