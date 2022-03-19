import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 1~N의 수열이 주어진다 (순서는 랜덤)
    # 이 수열의 맨 왼쪽 또는 맨 오른쪽만 골라서 증가 수열을 만들어야 한다.
    # 숫자를 고르면 그 숫자는 '소비'된다.
    정답 = 0
    정답2 = ''
    
    N = int(input())
    order = list(map(int, input().split()))
    latest = 0 # 가장 최근에 넣은 수
    
    for _ in range(N):
        left = order[0]
        right = order[-1]
        
        # 왼쪽 오른쪽 둘 다 가장 최근에 넣은 수보다 크면 작은 쪽을 먼저 넣는다
        # 한쪽만 큰 경우에는 그 쪽만 넣고 둘 다 작으면 종료
        if left > latest and right > latest:
            if left < right:
                latest = order.pop(0)
                정답 += 1
                정답2 += 'L'
            else:
                latest = order.pop()
                정답 += 1
                정답2 += 'R'
        elif left > latest: 
            latest = order.pop(0)
            정답 += 1
            정답2 += 'L'
        elif right > latest:
            latest = order.pop()
            정답 += 1
            정답2 += 'R'
        else:
            break

        
    정답 = str(정답)

#============================================================================#

    END = time()
    ANSWER = [정답,정답2]
    REAL_ANSWER = list(map(lambda x: x.strip(), open(pwd + f"\\out{FILE_NO}.txt", 'r').readlines()))

    if ANSWER == REAL_ANSWER:
        print("정답")
    else:
        print("오답")
        print(ANSWER, REAL_ANSWER)
    print(f"실행시간: {END - START}")
