import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

def 랜선_갯수_계산(자르는길이, 랜선들):
    갯수 = 0
    
    for 랜선 in 랜선들:
        갯수 += 랜선 // 자르는길이

    return 갯수

for i in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{i}.txt", 'r')

    K, 목표갯수 = map(int, input().split()) 
    랜선들 = [int(input()) for _ in range(0, K)]
    시작길이, 끝길이 = 1, max(랜선들)
    만든갯수 = -1

    while 시작길이 <= 끝길이:
        중간길이 = int((시작길이 + 끝길이) / 2)

        만든갯수 = 랜선_갯수_계산(중간길이, 랜선들)

        if 만든갯수 < 목표갯수:
            끝길이 = 중간길이 - 1
        else:
            시작길이 = 중간길이 + 1

    END = time()
    if 끝길이 == int(open(pwd + f"\\out{i}.txt", 'r').readline()):
        print("정답")
    else:
        print("오답")
    print(f"실행시간: {END - START}")
