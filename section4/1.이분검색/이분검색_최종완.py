import sys

pwd = __file__[0:__file__.rfind("\\")] # 모듈위치

for i in range(1,6): # i는 파일번호
    sys.stdin = open(pwd + f"\\in{i}.txt", 'r')
    n, M = map(int, input().split())
    배열 = [map(int, input().split())]
    print(배열)

    배열 = list(sorted(배열))
    시작점, 중간점, 끝점  = 0, -1, len(배열)-1

    while 배열[중간점] != M:
        중간점 = int((시작점 + 끝점) / 2)

        
        if(배열[중간점] > M):
            끝점 = 중간점
        else:
            시작점 = 중간점

    중간점 += 1

    if 중간점 == int(open(pwd + f"\\out{i}.txt", 'r').readline()):
        print("정답")
    else:
        print("오답")