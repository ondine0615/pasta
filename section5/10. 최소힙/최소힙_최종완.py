import heapq
import sys
from time import time


pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 이게 최소힙이랑은 전혀 관련이 없어보이는 문제임...
    # 나는 직접 힙을 구현하기 귀찮으므로 (사실 트리 순회를 할 줄 알아야 구현 할 수 있을 것 같음)
    # heapq를 사용한다.
    # heapq는 자료구조가 아니라 리스트를 힙처럼 다루게 해주는 모듈이다, 운용방식이 특이함.

    정답 = []
    tree = []

    while True:
        command = int(sys.stdin.readline().rstrip())

        if command == 0:
            정답.append(heapq.heappop(tree))
        elif command == -1:
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
