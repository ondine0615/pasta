import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for i in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{i}.txt", 'r')

#============================================================================#
    # (중요!) 여기서는 회의가 끝나는 시간으로 정렬해야한다

    # 패배 요인
    # 최대한 짧은 시간으로 생각함...

    정답 = -1
    
    n = int(input())
    예약희망 = [list(map(int, input().split())) for _ in range(n)]

    #회의 시간에 따라 정렬함
    예약희망.sort(key = lambda x :x[0])
    예약희망.sort(key = lambda x: x[1])
    
    예약 = [예약희망[0]]
    정답 = 1

    for 시작, 종료 in 예약희망:
        if 시작 >= 예약[정답-1][1]:
            정답 += 1
            예약.append([시작, 종료])

    print(정답)
        

#============================================================================#

    END = time()
    if 정답 == int(open(pwd + f"\\out{i}.txt", 'r').readline()):
        print("정답")
    else:
        print(정답, open(pwd + f"\\out{i}.txt", 'r').readline())
        print("오답")
    print(f"실행시간: {END - START}")
