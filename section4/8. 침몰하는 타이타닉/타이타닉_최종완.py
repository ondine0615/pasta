import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for FILE_NO in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{FILE_NO}.txt", 'r')

#============================================================================#
    # 구명보트당 Mkg 이하로 2명까지의 승객을 최대한 욱여넣는 방법
    정답 = 0
    
    N, M = map(int,input().split()) # N 승객수(5~1000), M 무게제한(70~250)
    weights = list(map(int, input().split())) # 승객 몸무게

    #그리디는 항상 어떤 것을 기준으로 정렬한다.
    weights.sort(reverse=True) #박스 높이의 내림차순으로 정렬

    #이제부터 승객을 태워보자 
    for i in range(0, N):
        try:
            load = weights[i]
            정답 += 1
            if load + weights[len(weights) - 1] <= M: #(POINT)배열의 오른쪽 끝에 있는 승객이 항상 가장 가볍다.
                weights.pop() #태울 수 있다면 가장 가벼운 승객을 배열에서 꺼낸다
        except IndexError:
            break
        
    print(정답)
        

#============================================================================#

    END = time()
    if 정답 == int(open(pwd + f"\\out{FILE_NO}.txt", 'r').readline()):
        print("정답")
    else:
        print(정답, open(pwd + f"\\out{FILE_NO}.txt", 'r').readline())
        print("오답")
    print(f"실행시간: {END - START}")
