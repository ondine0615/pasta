import heapq
import sys
from time import time


pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#

    정답 = []
    tree = []

    while True:
        command = int(sys.stdin.readline().rstrip()) * -1

        if command == 0:
            정답.append(abs(heapq.heappop(tree)))
        elif command == 1:
            break
        else:
            # heapq 자체가 자료구조가 아님에 유의
            heapq.heappush(tree, command)
        
    
#============================================================================#

    END = time()
    REAL_ANSWER = list(map(lambda s: int(s.rstrip()), open(pwd + f"\\out{FILE_NO}.txt", 'r').readlines()))

    if 정답 == REAL_ANSWER:
        print("정답")
    else:
        print("오답")
    print(f"실행시간: {END - START}")
