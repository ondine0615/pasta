import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 1~N의 수열 a이 주어진다 (순서는 랜덤)
    # 이 수열의 맨 왼쪽 또는 맨 오른쪽만 골라서 증가 수열을 만들어야 한다.
    # 역수열은 An = (수열a에서 n의 완쪽 중 an보다 큰 개수)
    # 주어진 역수열 갖고 원래의 수열을 만들어라.


    정답 = ''
    
    N = int(input())
    order = list(map(int, input().split()))
    original_order = [N+1 for _ in range(N)]
    
    for x in range(1, N+1): # x는 배치할 숫자
        cnt = 0 #배열 순회할 때 배치할 숫자가 이미 배치된 숫자보다 커야 증가
        pos = 0 #밑의 루프를 돌 때 마다 계~속 증가
        limit = order[x-1] # 역수열의 항을 제한하는 수로 취급
        for num in original_order: # num은 배치된 숫자
            if cnt == limit and original_order[pos] == N+1:
                original_order[pos] = x
                break
            if num > x: #(POINT!)이미 배치된 숫자는 항상 배치할 숫자보다 작다
                cnt += 1
            pos += 1
        
    정답 = " ".join(map(str, original_order))

#============================================================================#

    END = time()
    REAL_ANSWER = open(pwd + f"\\out{FILE_NO}.txt", 'r').readline().rstrip()

    if 정답 == REAL_ANSWER:
        print("정답")
    else:
        print("오답")
        print(정답)
        print(REAL_ANSWER)
    print(f"실행시간: {END - START}")
