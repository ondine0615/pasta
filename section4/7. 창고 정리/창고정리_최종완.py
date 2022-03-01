import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for i in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{i}.txt", 'r')

#============================================================================#
    # 가장 높은 열과 낮은 열의 높이 차를 최소화해야한다.
    # 가장 높은 열이 낮은 열에게 주면 된다.
    정답 = 1
    
    L = int(input()) 
    columns = list(map(int, input().split())) # 박스 높이
    M = int(input()) #높이 조정 횟수

    #그리디는 항상 어떤 것을 기준으로 정렬한다.
    columns.sort(reverse=True) #박스 높이의 내림차순으로 정렬

    #이제부터 박스를 옮겨보자 
    for _ in range(M):
        source = columns.index(max(columns))
        dest = columns.index(min(columns))
        
        columns[source] -= 1
        columns[dest] += 1
        
    정답 = max(columns) - min(columns)
    print(정답)
        

#============================================================================#

    END = time()
    if 정답 == int(open(pwd + f"\\out{i}.txt", 'r').readline()):
        print("정답")
    else:
        print(정답, open(pwd + f"\\out{i}.txt", 'r').readline())
        print("오답")
    print(f"실행시간: {END - START}")
