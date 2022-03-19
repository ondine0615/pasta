from collections import deque
import sys
from time import time


pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # circular Queue에서 순회를 실시한다
    # 순회마다 A +=1
    # A == K 시 A = 0 및 해당 원소를 큐에서 제외
    # 최후에 남게 되는 원소는?
    
    정답 = 0
    
    N, K = map(int, input().split())
    order = deque(range(1, N+1))
    count = 0

    while N > 1:
        temp = deque()

        for char in order:
            count += 1
            if count != K:
                temp.append(char)
            else:
                count = 0

        order = temp
        N = len(order)

    정답 = order.popleft()

#============================================================================#

    END = time()
    REAL_ANSWER = open(pwd + f"\\out{FILE_NO}.txt", 'r').readline().rstrip()

    if int(정답) == int(REAL_ANSWER):
        print("정답")
    else:
        print("오답")
        print(정답)
        print(REAL_ANSWER)
    print(f"실행시간: {END - START}")
