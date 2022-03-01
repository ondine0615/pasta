import sys
from time import time

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for i in range(1,6): # i는 파일번호
    START = time()
    sys.stdin = open(pwd + f"\\in{i}.txt", 'r')

#============================================================================#
    # 씨름선수를 뽑으려면 키와 몸무게 둘 중 하나는 커야 한다
    # 다시말해 완벽한 상위호환이 있는 선수는 탈락!

    정답 = 1
    
    n = int(input())
    wrestlers = [list(map(int, input().split())) for _ in range(n)] #씨름선수의 명단

    #그리디는 항상 어떤 것을 기준으로 정렬한다.
    wrestlers.sort(key=lambda x: x[0], reverse=True) #키의 내림차순으로 정렬한다
    passed_latest = wrestlers.pop(0)

    #이제부터 비교 들어간다 
    for height, weight in wrestlers:
        # 뽑히려면? 몸무게가 최근에 뽑힌 사람보다 신기록을 세워야 한다.
        # 키가 큰 선수가 먼저 이 조건문을 거치기 때문에 가능하다.
        if passed_latest[1] < weight:
            passed_latest = [height, weight]
            정답 += 1


    print(정답)
        

#============================================================================#

    END = time()
    if 정답 == int(open(pwd + f"\\out{i}.txt", 'r').readline()):
        print("정답")
    else:
        print(정답, open(pwd + f"\\out{i}.txt", 'r').readline())
        print("오답")
    print(f"실행시간: {END - START}")
