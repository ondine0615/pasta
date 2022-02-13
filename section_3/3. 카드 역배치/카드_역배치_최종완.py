import re
import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치


for file_no in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{file_no}.txt", 'r')

#============================================================================#

    정답 = ""
    배열 = [x for x in range(1,21)]
    
    뒤섞기 = [map(int, input().split()) for _ in range(0,10)]

    for a, b in 뒤섞기:
        임시 = 배열[0:a-1]

        for i in reversed(배열[a-1:b]):
            임시.append(i)
        
        for i in range(b, 20):
            임시.append(배열[i])
        배열 = 임시

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
